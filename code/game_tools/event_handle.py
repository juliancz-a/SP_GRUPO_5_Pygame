def button_click_event (event, assets_cfg):
    
    selection = None
    button_selected = 0
    
    for asset in assets_cfg:
        if asset["interaction"] == True:
            retorno = asset["box"].interaction(event)

            if retorno:
                selection = button_selected
                break

            button_selected += 1
    
    return selection