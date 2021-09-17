const arrow = document.getElementById('arrow');

document.getElementById('coin').addEventListener('mouseenter', () =>
    arrow.style.transform = 'rotate(180deg)'
);

document.getElementById('nft-token').addEventListener('mouseenter', () =>
    arrow.style.transform = 'rotate(0deg)'
);