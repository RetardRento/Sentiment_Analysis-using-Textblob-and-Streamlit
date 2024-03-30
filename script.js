const emoji = document.getElementById("sentiment-emoji");

anime({
  targets: emoji,
  scale: [1, 1.2, 1], // Scale up and down
  duration: 1000, // Animation duration in milliseconds
  easing: "easeInOutSine", // Animation easing function
  loop: true, // Continuously loop the animation
});
