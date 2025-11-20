# Initial Imports
import kagglehub
import shutil

# Download latest version
data_file_name = "mxmh_survey_results.csv"
local_source = (
    kagglehub.dataset_download("catherinerasgaitis/mxmh-survey-results")
    + "\\"
    + data_file_name
)
local_dest = "mental_health_music/data/mxmh_survey_results.csv"

# Transfer to directory
shutil.copy(local_source, local_dest)
