#!/bin/bash
# waits for the Urdu fix job on homidev, fetches it, then builds Urdu chapters and Urdu episodes/compiled
SP=/tmp/claude-1000/-mnt-storage-projects-LLMcourse/4f51127c-01bf-45ff-90cf-1e058f8384f8/scratchpad
K="-i $HOME/.ssh/id_ed25519 -o BatchMode=yes"
for i in $(seq 1 120); do
  S=$(timeout 30 ssh $K homidev@192.168.100.123 "python3 -c \"import json;print(json.load(open('assets/jobs/hominas/digcareer-urdu-fix-01/status.json'))['state'])\"" 2>/dev/null)
  echo "$(date +%H:%M) fix job state: $S"
  [ "$S" = done ] && break
  [ "$S" = failed ] && { echo "fix job FAILED"; exit 1; }
  sleep 60
done
[ "$S" = done ] || { echo "timed out waiting"; exit 1; }
mkdir -p ~/ai-inbox/digital-career-course/_urdu_voxcpm2 && cd ~/ai-inbox/digital-career-course/_urdu_voxcpm2 && rsync -a -e "ssh -i $HOME/.ssh/homidev_pull -o BatchMode=yes" homidev@192.168.100.123:hominas/digcareer-urdu-fix-01/ ./digcareer-urdu-fix-01/ && ls digcareer-urdu-fix-01/wav | wc -l && cd $SP/src && SP=$SP $SP/venv/bin/python make_urdu.py && SP=$SP $SP/venv/bin/python make_compiled.py ur && echo "URDU BUILD COMPLETE"
