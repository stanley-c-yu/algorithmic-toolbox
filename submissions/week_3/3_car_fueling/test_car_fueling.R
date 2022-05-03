library(testthat)
source("C:/Users/syu01/Documents/code/algorithms/submissions/week_3/3_car_fueling/car_fueling.R")

test_that("Test One", {
  expect_equal(compute_min_refills(950, 400, c(200, 375, 550, 750)), 2)
})

test_that("Test Two", {
  expect_equal(compute_min_refills(10, 3, c(1,2,5,9)), -1)
})

test_that("Test Three", {
  expect_equal(compute_min_refills(200, 250, c(100,150)), 0)
})