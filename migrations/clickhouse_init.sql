-- clickhouse_init.sql
CREATE DATABASE IF NOT EXISTS machine_learning;

CREATE TABLE IF NOT EXISTS machine_learning.predictions (
  id UUID DEFAULT generateUUIDv4(),
  sepal_length Float32,
  sepal_width Float32,
  petal_length Float32,
  petal_width Float32,
  predicted_class String,
  update_time DateTime DEFAULT now(),
  create_time DateTime DEFAULT now()
)
ENGINE = MergeTree()
ORDER BY id;
