const API_URL = "https://guaranteed-rose-ago-candy.trycloudflare.com"

async function getData(){
    try {
        const response = await fetch(`${API_URL}/battery`)

        if (!response.ok) {
            throw new Error(`Erro HTTP: ${response.status}`)
        }

        const data = await response.json()
        console.log(`Data:\n${data}`)

        let percent = data.percent.toFixed(0)
        document.getElementById("number-percent").textContent = `${percent}`

        document.getElementById("power-paragraph").textContent = data.power_plugged ? "Carregando" : "Sem carregar"

        document.getElementById("minutes").textContent = `${data.estimate.toFixed(0)}`

        const battery_icon = document.getElementById("battery-icon")
        const percent_paragraph = document.getElementById("percent-paragraph")

        if (percent <= 29 && !data.power_plugged) {
            battery_icon.style.color = "red"
            percent_paragraph.style.color = "red"
        } else if (30 <= percent <= 89 && !data.power_plugged) {
            battery_icon.style.color = "orange"
            percent_paragraph.style.color = "orange"
        } else {
            battery_icon.style.color = "green"
            percent_paragraph.style.color = "green"
        }

        const plug_icon = document.getElementById("plug-icon")
        const power_paragraph = document.getElementById("power-paragraph")

        if (data.power_plugged) {
            plug_icon.style.color = "green"
        } else {
            plug_icon.style.color = "black"
        }

        if (percent === 100) {
            document.getElementById("percent-defination").textContent = "Bateria Cheia!"
        } else {
            document.getElementById("percent-defination").textContent = ""
        }

    } catch (erro) {
        console.error("Falha na requisição:", erro);
    }
}

getData()