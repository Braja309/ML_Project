from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.constant import get_current_time_stamp

def main():
    try:

        pipeline = Pipeline(config= Configuration(current_time_stamp=get_current_time_stamp()))
        print(pipeline.get_experiments_status())
        #pipeline.start()
        #pipeline.run_pipeline()
        #data_validation_config = Configuration().get_data_validation_config()
        #print(data_validation_config)
        #data_transformation_config = Configuration().get_data_transformation_config()
        #print(data_transformation_config)
        #schema_file_path = r"C:\Users\Braja\Desktop\Data Science\ineuron Class\Projects\ML_Project\config\schema.yaml"
        #file_path = r"C:\Users\Braja\Desktop\Data Science\ineuron Class\Projects\ML_Project\housing\artifact\data_ingestion\2022-07-08-20-59-35\ingested_data\train\housing.csv"

        #df = DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()