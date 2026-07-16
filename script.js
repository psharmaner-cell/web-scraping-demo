document.addEventListener('DOMContentLoaded', () => {
  const footer = document.querySelector('footer p');
  if (footer) {
    footer.textContent = `Created by psharmaner-cell • ${new Date().getFullYear()}`;
  }
});
