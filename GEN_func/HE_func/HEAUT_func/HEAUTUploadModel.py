# This will upload automation models


def HEAUTUploadModel(em,model):


    # Select 1 (Host Encyclopedia functions )
    em.app.ispf_command("1")
    em.screen.log()
    assert em.screen.contains("TIEUTILS"), "Automation Upload Upload Model: Host Encyclopedia not found"

    # Select 3 (Model Management )
    em.app.ispf_command("3")
    em.screen.log()
    assert em.screen.contains("TIEA12"), "Automation Upload Upload Model: Model Management not found"


    em.app.ispf_command("16")
    # Select 4 (Upload Model )
    assert em.screen.contains("TIEUP"), "Automation Upload Upload Model: Upload Model/Subset not found"
    em.screen.log()
    em.screen['Transaction file name'] = 'AG86.QA.MODELS.AUT.S92A6'+'('+ model + ')'
    em.screen['Execution mode'] = '/'
    em.screen[3] = '.'
    em.screen.log()
    em.submit_screen()
    em.submit_screen(wait_for_text="IEF OK")
    assert em.screen.contains("All processing completed normally"), "Automation Upload Upload Model: Upload failed"
    em.screen.log()
    em.submit_screen("PF3")
    em.screen.log()
    em.submit_screen("PF3")
    em.screen.log()
    em.submit_screen("PF3")
    em.screen.log()