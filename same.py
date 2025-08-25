!DOCTYPE html
html
head
  titleOBS Virtual Camera Testtitle
head
body
  h1OBS Virtual Camera Feedh1
  video id=video autoplay playsinlinevideo

  script
    async function startCamera() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video true });
        document.getElementById('video').srcObject = stream;
      } catch (err) {
        console.error(Error accessing camera, err);
      }
    }
    startCamera();
  script
body
html
