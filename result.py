class Result:
    def __init__(self, caption, points):
        self.caption = caption
        self.points = int(points)

    def __str__(self):
        return self.caption

if __name__ == "__main__":
  result_image = "inflatable_trex"
  total_points = 25 #Baseline points required for this result
  caption = "Inflatable TRex wants to blend in, keep up with the crowd, but he feels like something is missing . . ."
  result1 = Result(caption, total_points)
  print(result1)
