library(testthat)
source("C:/Users/syu01/Documents/code/algorithms/submissions/week_3/7_maximum_salary/largest_number.R")

test_that("23 and 3", {
  expect_equal(largest_number(c(23, 3)), "323")
})

test_that("21 and 2", {
  expect_equal(largest_number(c(21, 2)), "221")
})

test_that("9, 4, 6, 1, 9", {
  expect_equal(largest_number(c(9,4,6,1,9)), "99641")
})

test_that("23, 39, 92", {
  expect_equal(largest_number(c(23, 39, 92)), "923923")
})


