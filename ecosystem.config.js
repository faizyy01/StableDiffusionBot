module.exports = {
  apps: [
    {
      name: "Stable Diffusion Telegram",
      script: "/home/faiz/builds/StableDiffusionBot/venv/bin/python",
      args:
        "main.py",
      watch: false,
      interpreter: "",
    }
  ]
};
