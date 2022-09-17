if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/PR0FESS0R-99/Adv-Information-Bot.git /Adv-Information-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Adv-Information-Bot
fi
cd /ID-Bot-V1
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 motech.py
