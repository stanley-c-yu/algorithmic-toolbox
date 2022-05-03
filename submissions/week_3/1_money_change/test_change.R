library(testthat)
source("C:/Users/syu01/Documents/code/algorithms/submissions/week_3/1_money_change/change.R")

test_that("Test One", {
  expect_identical(get_change(2), 2)
})

test_that("Test Two", {
  expect_identical(get_change(28), 6)
})

