from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# logging.INFO("Start Spark Session")
spark = SparkSession.builder.getOrCreate()

# sparkConf = SparkConf().setMaster("local").setAppName("Guess Who Spark Job")
# sparkContext = SparkContext(conf=sparkConf)

# spark = sparkContext.getOrCreate()

# logging.INFO("Create Spark Dataframe of persons")
personDf = spark.createDataFrame(
    [
        ( "Alex", 0, 0 ),
        ( "Alfred", 0, 1 ),
        ( "Anita", 0, 2 ),
        ( "Anne", 0, 3 ),
        ( "Bernard", 0, 4 ),
        ( "Bill", 0, 5 ),
        ( "Charles", 0, 6 ),
        ( "Claire", 0, 7)
    ],
    schema="Name string, Row int, Col int"
)
