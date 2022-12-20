from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# logging.INFO("Start Spark Session")
spark = SparkSession.builder.getOrCreate()

# sparkConf = SparkConf().setMaster("local").setAppName("Guess Who Spark Job")
# sparkContext = SparkContext(conf=sparkConf)

# spark = sparkContext.getOrCreate()

# logging.INFO("Create Spark Dataframe of persons")
