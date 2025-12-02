import os

def create_structure(base_dir, structure):
    for path in structure:
        full_path = os.path.join(base_dir, path)
        if path.endswith("/"):
            os.makedirs(full_path, exist_ok=True)
            # create placeholder
            open(os.path.join(full_path, ".gitkeep"), "w").close()
        else:
            # create file
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            open(full_path, "w").close()

project1 = {
    "Execution-Algorithms-Suite/README.md",
    "Execution-Algorithms-Suite/requirements.txt",

    "Execution-Algorithms-Suite/config/algo_config.yaml",
    "Execution-Algorithms-Suite/config/model_config.yaml",

    "Execution-Algorithms-Suite/data/LOB/",
    "Execution-Algorithms-Suite/data/trades/",
    "Execution-Algorithms-Suite/data/intraday/",
    "Execution-Algorithms-Suite/data/output/",

    "Execution-Algorithms-Suite/src/algos/vwap.py",
    "Execution-Algorithms-Suite/src/algos/twap.py",
    "Execution-Algorithms-Suite/src/algos/pov.py",
    "Execution-Algorithms-Suite/src/algos/implementation_shortfall.py",

    "Execution-Algorithms-SSuite/src/microstructure/ofi.py",
    "Execution-Algorithms-Suite/src/microstructure/volatility_models.py",
    "Execution-Algorithms-Suite/src/microstructure/depth_features.py",

    "Execution-Algorithms-Suite/src/impact/almgren_chriss.py",
    "Execution-Algorithms-Suite/src/impact/impact_calibration.py",

    "Execution-Algorithms-Suite/src/models/lstm_signal.py",
    "Execution-Algorithms-Suite/src/models/random_forest_signal.py",
    "Execution-Algorithms-Suite/src/models/linear_signal.py",

    "Execution-Algorithms-Suite/src/backtester/simulator.py",
    "Execution-Algorithms-Suite/src/backtester/slippage.py",

    "Execution-Algorithms-Suite/src/utils/loaders.py",
    "Execution-Algorithms-Suite/src/utils/plotting.py",

    "Execution-Algorithms-Suite/src/main.py",

    "Execution-Algorithms-Suite/notebooks/01_feature_extraction.ipynb",
    "Execution-Algorithms-Suite/notebooks/02_signal_model_demo.ipynb",
    "Execution-Algorithms-Suite/notebooks/03_execution_backtest.ipynb",
    "Execution-Algorithms-Suite/notebooks/04_market_impact_calibration.ipynb",
}

create_structure("", project1)