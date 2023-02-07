function toggleLED(color){
  console.log(color);
    fetch(`/toggle-led/${color}`)
    .then(response => {
        console.log(response)
    })
    .catch(error => {
        console.log(error)
    });
}
