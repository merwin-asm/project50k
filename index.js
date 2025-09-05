const nameInput = prompt('Enter your Name')
const dialogue = document.querySelector('a-text')
const input = document.getElementById('input')

const camera = document.querySelector('a-camera')

const monScreen = document.getElementById('a-plane-form')

monScreen.addEventListener('onclick', () => {
    monScreen.attributes.scale = '1 1 1'
})

async function setScene () {
    const response = await fetch(`http://127.0.0.1:8000/bot_reply`, {
        method: 'GET',
        mode: 'cors', 
        headers: {
            'name': nameInput
        }
    })

    const data = await response.text()
    dialogue.attributes.value.nodeValue = data
}

window.onload = setScene

let count = 1

async function userInput() {
    let text = ''
    window.addEventListener('keydown', async (e) => {

        if (e.key.length === 1) {
            text += e.key
        } else if (e.key === 'Backspace') {
            text = text.slice(0, -1);
        } else if (e.key === 'Enter') {
            const response = text

            const request = await fetch('http://127.0.0.1:8000/user_reply', {
                method: 'GET',
                mode: 'cors',
                headers: {
                    'text': response,
                    'name': nameInput
                }
            }).then(async () => {
                const response = await fetch(`http://127.0.0.1:8000/bot_reply`, {
                    method: 'GET',
                    mode: 'cors', 
                    headers: {
                        'name': nameInput
                    }
                })
                const data = await response.text()
                console.log(data)

                dialogue.attributes.value.nodeValue = data

                if (count < 6) {
                    setInterval(() => window.location.reload(), 5000)
                    count = count + 1
                } else {
                    alert('The simulation is over')
                }
            })
        }

        input.setAttribute('value', text)
    })
}

setInterval(userInput(), 3000)