test = {
  'name': 'Question 1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(parameters)
          3
          >>> np.isclose(parameters.item(0), 0.8343076972837598)
          True
          >>> np.isclose(parameters.item(1), 0.09295728160512184)
          True
          >>> np.isclose(parameters.item(2), -1.566520972963474)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
