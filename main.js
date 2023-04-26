const { app, BrowserWindow, ipcMain, shell } = require('electron');
const path = require('path')


function createWindow () {
  const win = new BrowserWindow({
    width: 1600,
    height: 800,
    icon: path.join(__dirname, 'icon.png'),
    autoHideMenuBar: true,
    webPreferences: {
      nodeIntegration: true
    }
  })

  
  win.loadFile('index.html')
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

ipcMain.on('open-batch-file', (event, batchFilePath) => {
  shell.openItem(batchFilePath, { runAsAdmin: true });
});