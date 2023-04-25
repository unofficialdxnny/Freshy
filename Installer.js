// const { spawn } = require('child_process');
// 
// // get the button element
// const button = document.getElementById('firefox');
// 
// // add a click event listener to the button
// button.addEventListener('click', () => {
//   // run the choco command to install the package
//   const child = spawn('choco', ['install', 'firefox', 'y'], {
//     detached: false,
//     stdio: 'ignore'
//   });
// 
//   // unref the child process
//   child.unref();
// });
// 

const { ipcRenderer } = require('electron');

// Send a message to the main process to open the batch file
ipcRenderer.send('open-batch-file', app.getAppPath() + 'chocoInstall.bat');
