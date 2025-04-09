from src.config import load_config
from src.ga.engine import run_evolution

def main():
    config = load_config('config/default.yaml')
    run_evolution(config)

if __name__ == '__main__':
    main()