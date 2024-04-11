from calculator import Sheet, Cell
           
if __name__=="__main__":
  s=Sheet(5,5)
  print()

  s.set('A1','A2')
  s.set('A2','A5')
  s.set('A3','A1+A2')
  s.set('A5','2')
  s.print()
  print()

  s.set('A1','4')
  s.set('A4','A1+A3')
  s.set('A6','10')
  s.print()
  print()

  s.set('A1','A3')
  s.print()
  print()