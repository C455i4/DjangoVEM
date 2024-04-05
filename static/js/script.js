// Função para animar o contador
function animateCount(element, start, end, duration) {
    let range = end - start;
    let current = start;
    let increment = end > start ? 1 : -1;
    let stepTime = Math.abs(Math.floor(duration / range));
    let timer = setInterval(function() {
        current += increment;
        element.textContent = current;
        if (current == end) {
            clearInterval(timer);
        }
    }, stepTime);
}

// Inicia a animação dos contadores
window.onload = function() {
    let contadorMeninas = document.getElementById('contadorMeninas');
    let contadorCompras = document.getElementById('contadorCompras');
    
    // Suponha que você tenha os valores reais de visitantes e compras
    let meninas = 110;
    let comprasReais = 240;
    
    // Chame a função para animar os contadores
    animateCount(contadorMeninas, 0, meninas, 2000); // 2000 milissegundos (2 segundos) de duração da animação
    animateCount(contadorCompras, 0, comprasReais, 2000);
};
