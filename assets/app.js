document.addEventListener('DOMContentLoaded', () => {
    // Track page
    let addRideBtn = document.querySelector('.add-ride')
    let qrCode = document.querySelector('.qr-code')

    addRideBtn.addEventListener('click', () => {
        console.log('clicked')
        qrCode.style.display = 'block'
    })
})