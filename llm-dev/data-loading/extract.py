import requests
import tarfile
import io

def downloadAndExtract():
    # Step 1: Specify the URL of the .tar.gz file
    url = "https://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz"

    # Step 2: Fetch the file using requests
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Ensure the request was successful

    # Step 3: Open the .tar.gz file from the response content
    with tarfile.open(fileobj=io.BytesIO(response.content), mode="r:gz") as tar:
        # Step 4: Extract the contents
        tar.extractall(path="movieData")  # Change path as needed
        print("Extraction complete. Files are saved in 'movieData' directory.")

    # Optional: List the files in the archive
        file_names = tar.getnames()
        print("Files in the archive:", file_names)
