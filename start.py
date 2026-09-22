#!/usr/bin/env python3
import sys

import uvicorn


def main():
    # Detect environment from command-line arguments (default: "dev")
    env = sys.argv[1] if len(sys.argv) > 1 else "dev"

    if env == "prod":
        # Optimized configuration for Production
        print("🚀 Starting FastAPI in PRODUCTION mode...")
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            workers=4,  # Multiple processes according to the server's cores
            reload=False,
            log_level="info",
        )
    else:
        # Configuration for Development
        print("🛠️  Starting FastAPI in DEVELOPMENT mode (Hot Reload active)...")
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="debug",
        )


if __name__ == "__main__":
    main()