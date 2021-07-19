from slack_bolt import App

from env_vars import SLACK_APP_PORT, SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET

# Initializes your app with your bot token and signing secret
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)

# Add functionality here
@app.event("message")
def handle_message(client, event, logger):
  try:
      if 
      print("Hamster")
  
  except Exception as e:
    logger.error(f"Error handling message: {e}")


# Start your app
if __name__ == "__main__":
    app.start(port=SLACK_APP_PORT)