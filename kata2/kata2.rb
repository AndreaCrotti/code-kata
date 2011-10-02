#!/usr/bin/env ruby -w
$VERBOSE = true
$DEBUG = true

require 'rubygems'
require 'test/unit'

def mid_point(first, last)
  first + ((last - first) / 2)
end

def chop(idx, arr)
  false if arr.empty?
  
  puts "arr = #{arr.to_s}"
  mid = mid_point(0, arr.length)
  puts mid
  val = arr[mid]
  mid if val == idx

  if val > idx
    puts "slicing 0, #{mid}"
    left = arr.slice(0, mid)
    chop(idx, left)
  else
    puts "slicing #{mid+1}, #{arr.length}"
    right = arr.slice(mid+1, arr.length)
    chop(idx, right)
  end
end

class TestKata2 < Test::Unit::TestCase
  def test_chop
    assert_equal(-1, chop(3, []))
    assert_equal(-1, chop(3, [1]))
    assert_equal(0,  chop(1, [1]))
    #
    assert_equal(0,  chop(1, [1, 3, 5]))
    assert_equal(1,  chop(3, [1, 3, 5]))
    assert_equal(2,  chop(5, [1, 3, 5]))
    assert_equal(-1, chop(0, [1, 3, 5]))
    assert_equal(-1, chop(2, [1, 3, 5]))
    assert_equal(-1, chop(4, [1, 3, 5]))
    assert_equal(-1, chop(6, [1, 3, 5]))
    #
    assert_equal(0,  chop(1, [1, 3, 5, 7]))
    assert_equal(1,  chop(3, [1, 3, 5, 7]))
    assert_equal(2,  chop(5, [1, 3, 5, 7]))
    assert_equal(3,  chop(7, [1, 3, 5, 7]))
    assert_equal(-1, chop(0, [1, 3, 5, 7]))
    assert_equal(-1, chop(2, [1, 3, 5, 7]))
    assert_equal(-1, chop(4, [1, 3, 5, 7]))
    assert_equal(-1, chop(6, [1, 3, 5, 7]))
    assert_equal(-1, chop(8, [1, 3, 5, 7]))
  end
end

