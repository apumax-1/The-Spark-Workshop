from pyspark.sql import SparkSession
from typing import Tuple
import re

novella_location = '/Users/a/IdeaProjects/The-Spark-Workshop/resources/HoD.txt'  # ToDo: change path

def create_session(num_threads: int=2, name: str="Spark Application") -> SparkSession:
    session: SparkSession = SparkSession.builder \
        .master('local[{}]'.format(num_threads)) \
        .appName(name) \
        .getOrCreate()
    return session #  // program simulates a single executor with numThreads cores (one local JVM with numThreads threads)


def get_neighbours(line: str):
    tokens = re.split('\\W+', line)
    return list(map(lambda token: (token, len(tokens)), tokens))


def calc_average(word_stats: Tuple[str, Tuple[int, int]]) -> Tuple[str, int]:
    word = word_stats[0]
    count = word_stats[1][0]
    neighbours = word_stats[1][1]
    average = neighbours / count
    return word, average
