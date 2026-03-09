# debug_tau2.py

from src.tau2.cli import main
import sys
import os
os.environ["OPENAI_API_KEY"] = "EMPTY"

if __name__ == "__main__":
    # sys.argv = [
    #     "tau2",
    #     "run",
    #     "--domain", "mock",      # 先用最小配置
    #     "--num-trials", "1",
    #     "--max-steps", "200",

    #     "--agent-llm", "openai/Qwen/Qwen3-4B",
    #     "--agent-llm-args", '{"api_base":"http://localhost:8000/v1", "temperature": 0.6}',

    #     "--user-llm", "openai/Qwen/Qwen3-8B", # gpt-4.1-mini
    #     "--user-llm-args", '{"api_base":"http://localhost:8001/v1", "temperature": 0.6}',
        
    #     "--save-to", "/scratch/pioneer/jobs/wxy320/save/agent/mock-trials1-steps200-Qwen3-4B-Qwen3-8B",
    #     "--log-level", "DEBUG"
    # ]

    ## no user
    sys.argv = [
        "tau2",
        "run",
        "--domain", "telecom",      # 先用最小配置
        "--num-trials", "1",
        "--max-steps", "200",

        "--agent-llm", "openai/Qwen/Qwen3-4B",
        "--agent-llm-args", '{"api_base":"http://localhost:8000/v1", "temperature": 0.6}',

        #  "--agent", "llm_agent_solo",
        # "--user", "dummy_user",
        "--user-llm", "openai/Qwen/Qwen3-8B", # gpt-4.1-mini
        "--user-llm-args", '{"api_base":"http://localhost:8001/v1", "temperature": 0.6}',
        
        "--save-to", "/scratch/pioneer/jobs/wxy320/save/agent/telecome-trials1-steps200-Qwen3-4B-Qwen3-8B",
        "--log-level", "DEBUG",
        "--max-concurrency", "1"
    ]

    main()