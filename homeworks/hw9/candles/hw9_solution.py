def count_candles(candle_number, make_new):
    total_burned = 0
    leftovers = 0

    while candle_number > 0:
        total_burned += candle_number
        leftovers += candle_number

        candle_number = leftovers // make_new
        leftovers = leftovers % make_new

    return total_burned
