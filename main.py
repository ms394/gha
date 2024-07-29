import sys

def main():
    if len(sys.argv) != 5:
        logger.info(f"Usage: python {sys.argv[0]} <source_project_name> <source_sa_client_secret> <target_project_name> <target_sa_client_secret>")
        return
    print('python')
    print("python: ",sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

    return




if __name__ == "__main__":
    main()
