$(document).ready(function() {
    
    // sending a connect request to the server.
    var socket = io.connect('http://127.0.0.1:5000');
    
    socket.on('load page', function(msg) {
        console.log('load page', msg);
        document.getElementById("title").innerText = msg.title;
        document.getElementById("description").innerText = msg.description;
        let log = document.getElementById("log");
        log.innerHTML = "";
        for(let subteam in msg.content) {
            log.innerHTML += "<H2>"+subteam+"<\H2>";
            for(let task of msg.content[subteam]) {
                console.log(task)
                log.innerHTML += '<input type="checkbox" id="vehicle1" name="vehicle1" value="' + task + '"><label for="vehicle1">' + task + '</label><br>'
                
            }
        }
    });        
});