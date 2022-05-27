timestamps {
    def builders = [:]

    def labels = ['zos-test']
    for (x in labels) {
        def label = x

        // Create a map to pass in to the 'parallel' step so we can fire all the builds at once
        builders[label] = {
            node(label) {
                stage('Generate & Test') {
                    // Clean the workspace
                    deleteDir()

                    // Checkout the source
                    checkout scm

                    // Perform the tests
                    boolean doPublish = false
                    try {
                        withEnv(["JAVA_HOME=C:\\java8_32"]) {
                            String procFile = env.PROCESS_FILE.trim()
                            if (procFile.length() > 0) {
                                println "Processing file: [" + procFile + "]"
                                bat "processMFTests.cmd ${procFile}"
                                doPublish = true
                            } else {
                                String mods = env.MODELS.trim()
                                if (mods.length() > 0) {
                                    String[] models = mods.split("\\s*,\\s*")
                                    if (models.size() > 0) {
                                        for (model in models) {
                                            model = model.trim()
                                            if (model.length() > 0) {
                                                println "Processing model: [" + model + "]"
                                                bat "runMFRegressionTests.cmd ${model}"
                                                doPublish = true
                                            }
                                        }
                                    }
                                } else {
                                    throw new Exception("Nothing to do, invalid Input. Please enter the name of a file to process or a comma separated list of model names.")
                                }
                            }
                        }
                    }
                    finally {
                        if (doPublish) {
                            // Publish results
                            archiveArtifacts allowEmptyArchive: true, caseSensitive: false, onlyIfSuccessful: false, artifacts: "Reports\\Test\\**\\*.*"
                        }
                    }
                }  // stage
            }  // node
        }  //builders
    }  // for

    try {
        parallel builders
        currentBuild.result = 'SUCCESS'
    } catch (Exception err) {
        println "${err}"
        currentBuild.result = 'FAILURE'
    }
    finally {
        println "Regression Testing Completed: ${currentBuild.result}"
    }
}
