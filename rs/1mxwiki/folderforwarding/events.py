def notifyFolderIsAdded(folder, event):
    folder.REQUEST.RESPONSE.redirect(folder.absolute_url() + "/++add++Document")
