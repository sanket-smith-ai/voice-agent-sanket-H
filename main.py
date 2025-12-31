from voice_loop import voice_loop

if __name__ == "__main__":
    stop_flag = {"stop": False}
    try:
        voice_loop(stop_flag)
    except KeyboardInterrupt:
        stop_flag["stop"] = True
        print("\nExiting...")
