export HF_TOKEN=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


CUDA_VISIBLE_DEVICES=0 nohup vllm serve Qwen/Qwen3-4B \
  --host 0.0.0.0 \
  --port 8000 \
  --gpu-memory-utilization 0.90 \
  --reasoning-parser qwen3 \
  --trust-remote-code \
  --enable-auto-tool-choice \
  --tool-call-parser hermes \
  > /home/wxy320/ondemand/program/tau2-bench/debug_vllm/user.log 2>&1 &

# curl http://localhost:8000/v1/models


