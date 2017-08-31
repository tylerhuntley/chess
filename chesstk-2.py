from tkinter import *

columns = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}
colors = {0:'white', 1:'black'}
icons = {
    'whitePawn': b'R0lGODlhIAAgAMYAAAAAAAEBAQICAgQEBAcHBwkJCQsLCwwMDBMTExUVFRgYGBwcHB4eHiEhISQk\nJCcnJysrKy4uLi8vLzY2Nj8/P0NDQ0hISExMTE1NTVNTU15eXmRkZGtra3BwcHJycnl5eX19fX9/\nf4eHh5ubm6enp62tra6urrCwsLKysry8vMHBwcTExMXFxcnJyc3Nzc/Pz9HR0dPT09jY2Nvb29/f\n3+Li4uXl5ejo6Orq6uzs7O3t7fDw8PLy8vf39/j4+Pn5+fr6+vv7+/39/f///wAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH+\nEUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAH8ALAAAAAAgACAAAAfegH+Cg4SFhoeIiYIaEBaKj4cD\nChsSACGQmAYVQkNDJAKYkAA6nZ0IoY8AO6VDCaiKBiOlNQCviQIapSmgtoYCG6xDKry9ggYZwZ0o\ntcV/ADzJna7NBtGdFM1/BTnWEdkALtE/xL0SDD/JGQTZfwQUnKUjzM0SAhY3pT0eBdO9Cgozou2Y\nQC5UAwXQrAmhsO6VARzWSgVxwAAVAVkRZ82DVABdxlISJGBCwOEjqxYbEwV4YbKUjwKYAOBr2WkB\npgNAaHaagKlAiJ9Agwr9WRESgqNIkypNyq6p06dQQwUCADs=\n',
    'whiteRook': b'R0lGODlhIAAgAKU0AAAAAAICAgUFBQYGBgcHBwsLCwwMDA0NDQ4ODhAQEBERERMTExUVFRgYGBsb\nGxwcHB4eHiMjIyQkJCcnJyoqKisrKzs7O0hISE1NTVNTU1RUVFxcXGRkZHl5eX9/f46OjpWVlZub\nm62trbCwsLKysre3t8XFxcnJyc3NzdHR0dXV1djY2N/f3+Li4urq6u3t7fDw8PLy8vX19ff39///\n/////////////////////////////////////////////yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5\nBAEKAD8ALAAAAAAgACAAAAb7wJ9wSCwaj8ikcslsLg8AQIAYjRIJ0QMTACIVLMLGhESaNIQZAAkE\n2L5olyrgQ6OJ5BPaq70EtOqAgYJ1M3xKAQcLiouMjQsHU0sLBBselpeYmBsEBk0TByJkoqOiIgdn\nTgoaKqytrqwaCk5CFhaDgxwQsz+1t4K5u72+gMCzwsM0xU7Hw8pNzL7OTNC30kvUuLrGtsjJ2k4J\nCxXj5OXjD1qzACfdNCyRTQIACPT19vYBAk4AFP3+/wAp6GsCoF2gBUwwTACAoaHDhxAxDJiAIQmD\nBREMaNzIsePGCA0QHlnA4YXJkyhTpgQh0ogEOTBjynSwq6bNmziVBAEAOw==\n',
    'whiteKnight': b'R0lGODlhIAAgAOeLAAAAAAICAgMDAwUFBQcHBwgICAkJCQsLCw0NDQ8PDxERERMTExUVFRcXFxgY\nGBoaGhsbGxwcHB0dHR4eHh8fHyAgICEhISIiIiMjIyQkJCUlJSYmJicnJygoKCkpKSoqKisrKyws\nLC0tLTAwMDExMTIyMjMzMzQ0NDY2Njc3Nzg4ODk5OTs7Ozw8PD09PT4+Pj8/P0BAQEFBQUNDQ0VF\nRUZGRkdHR0hISElJSUtLS0xMTE1NTU9PT1BQUFFRUVNTU1VVVVdXV1hYWFpaWltbW1xcXF5eXmRk\nZGdnZ2lpaWtra25ubnBwcHJycnNzc3d3d3l5eX19fX9/f4eHh4qKipCQkJGRkZOTk5WVlZubm52d\nnZ+fn6CgoKKioqWlpaenp6ysrK2trbGxsbW1tba2tre3t7u7u7y8vL6+vsHBwcXFxcfHx8nJyc3N\nzc7OztHR0dXV1dfX19jY2N3d3d7e3t/f3+Dg4OHh4eLi4uPj4+Xl5ejo6Orq6uvr6+3t7fDw8PLy\n8vPz8/T09PX19ff39/j4+Pn5+fr6+vv7+/39/f7+/v//////////////////////////////////\n////////////////////////////////////////////////////////////////////////////\n////////////////////////////////////////////////////////////////////////////\n////////////////////////////////////////////////////////////////////////////\n////////////////////////////////////////////////////////////////////////////\n////////////////////////////////////////////////////////////////////////////\n/////////////////////////////////////////////////////yH+EUNyZWF0ZWQgd2l0aCBH\nSU1QACH5BAEKAP8ALAAAAAAgACAAAAj+AP8JHEiwoMGDCAsCKEggocOCC6QYGGhEycOL/xYQoiLg\nXw9EXjBe1LJoypM3i+QYWSFB5EEBYhbJnJkHTQUGHTC4HEhjpk86MutIcVAigEsPcBYF8rlIj889\nMGYcEGllkRQvTA0xDfRDxsSHOWS+IMS0rNIRNB4iQGO2rUw0NS44HOL2rdkfPxIikFMXUcyyZXaI\nQGik7iIkfdpmEHIQBJu6ThzUaetkyEEkdSVeIGsWDI8JBQ2g5OwTEZKOMNzmSfCiYIhFc/7OnHOD\nYt0FeQmK6KxhIAMsdWPsKJhg6SIqKK0wICjDcA8cBnHUqYMiUJkFBFPIbmuktkEAAEpSUKlAkEEY\nw4uixEAgUgFW9FIqZMDYgQp6meM3YLR/v2SFERe9AEh/VlXwwUVJELgIFBWEcNEUCjpRwWAP2WDE\nhRhmqKERLoTwwE4ghijiiAgFBAA7\n',
    'whiteBishop': b'R0lGODlhIAAgAMZKAAAAAAICAgQEBAcHBwgICAkJCQsLCw0NDRAQEBERERMTExUVFRgYGBkZGRsb\nGx4eHiMjIyQkJCcnJysrKywsLC8vLzAwMDIyMjY2Njs7Oz09PT8/P0JCQkNDQ0dHR0hISE1NTVFR\nUVNTU1hYWF5eXmRkZGlpaWtra3Jycnl5eX9/f4eHh46OjpWVlZubm6Kioqenp62trbKysre3t7y8\nvMHBwcXFxcnJyc3NzdHR0dXV1djY2Nvb29/f3+Li4uXl5ejo6Orq6u3t7fDw8PLy8vT09PX19ff3\n9/n5+f39/f//////////////////////////////////////////////////////////////////\n////////////////////////////////////////////////////////////////////////////\n/////////////////////////////////////////////////////////////////////////yH+\nEUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAH8ALAAAAAAgACAAAAf+gH+Cg4SFhoeIiYIjK4qOiAAS\nCwWPlYIbGUpJCC+Wj5ianJ6PABQNlKOKKgMBAAoyqYgHBSlEPh8BErGFAxVHSsBKPwoKu4IBIknA\nO0HARRLFsQsVysAMKsFHCB2xA0PLMgkWMkLANgCpEh/BEwDuACvBCCmjADbBwA8l+EokE/U6+E1o\nwU/FP08CXvBbqOTDhVEZIjDEV2SAi1QBUlRbeOTCgV0BEkCYQLKkgwKoYjEwwAGEy5cWAoDYlaJA\nM4Y00MVqoEGGz59AGYSI9a6oUQALiMKYqGmEg1ggADxQISMHEB83YpxAEKDTrg8KBBQlwKBEKhEV\nSEJzl8CEhwFPAAQsKJmBRCJWCy68RLGiqhIkSZDQiKGixMsJCABUKBQgQ1YUL19uYBD3wYfILlfM\neFEAASEF7go4KFkSQwobM0qkJT1hAVwAGIzJnj0oEAA7\n',
    'whiteKing': b'R0lGODlhIAAgAMZcAAAAAAEBAQICAgMDAwQEBAUFBQYGBgcHBwoKCgsLCw0NDQ4ODg8PDxAQEBER\nERISEhMTExQUFBUVFRYWFhcXFxgYGBkZGRsbGxwcHB0dHR4eHiEhISQkJCUlJScnJygoKCsrKy8v\nLzAwMDIyMjQ0NDY2Njc3Nzk5OTs7Oz09PT4+Pj8/P0hISE1NTVNTU1VVVVdXV1hYWF5eXmRkZGtr\na2xsbG5ubnd3d3l5eX9/f46OjpGRkZWVlZubm5+fn6CgoKKioqampqenp6mpqa2tra6urrKysrS0\ntLe3t8HBwcXFxcnJydHR0dXV1dvb2+Li4uTk5OXl5ejo6Orq6u3t7fDw8PLy8vT09Pf39/n5+fv7\n+/39/f//////////////////////////////////////////////////////////////////////\n/////////////////////////////////////////////////////////////////////////yH+\nEUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAH8ALAAAAAAgACAAAAf+gH+Cg4SFhoeIiYMlio2JIB44\njpOCDUM+CSc7MJSNKxsAoQA3nYoCIz8QNi0NpY0oEDOujggGDrONCEAxuIoAXFy9iBPAXACzAgkj\nKBQAA4IYxcd/AwAUKCQMAAGHADhaxVIzAgIDWcAAAgAxUsVcSQkChQMv7sVPEgNEXFsLCUz2gEk5\nIE9QOiwBgVlxkCBLjQBOEgIDUvBPgF8SuVg5oGKAkIxcpEz7EwokFyEAHmwBGWUkgAQrM25RgMNk\nD26DBPQwCSEHyCsJDAlQArJnxiwcKg4KEAAIsCxKZJQAASEBAAUgWOBAAk4gBaWFAHQQQQBAhRIt\ncPAwksPFiAuLAg6wYFKkAFhDADgYqfITiAdjkwAYeUrlSRMlRpY0kUIlZgpKAF7I0KBOlGUABDzQ\nMAEZgIYZSppQoQIuC5UpTYy0qDCyUckrSXTQaAECxIi0PZac4xT4BAfMEDaEaEEchAYImENs6BQg\nQ5BzEq3kiNDaUbUPOYwwYfxkiRAcFgAUwFXuouXywoQFAgA7\n',
    'whiteQueen': b'R0lGODlhIAAgAMZiAAAAAAICAgMDAwQEBAUFBQcHBwgICAkJCQoKCgsLCwwMDA0NDQ8PDxAQEBER\nERMTExUVFRcXFxgYGBsbGx4eHiEhISMjIyQkJCUlJScnJysrKywsLC4uLi8vLzAwMDIyMjU1NTY2\nNjs7Oz09PT8/P0FBQUJCQkNDQ0hISExMTE1NTVFRUVNTU1VVVVhYWF5eXmRkZGlpaWtra2xsbG5u\nbnJycnl5eXt7e39/f4WFhYeHh46OjpWVlZubm6KioqOjo6enp6qqqq2trbKysrW1tbe3t7y8vMHB\nwcLCwsXFxcbGxsjIyMnJyc3Nzc/Pz9HR0dXV1djY2Nvb29/f3+Li4uPj4+Xl5ejo6Onp6erq6u3t\n7fDw8PLy8vT09PX19ff39/n5+f39/f//////////////////////////////////////////////\n/////////////////////////////////////////////////////////////////////////yH5\nBAEKAH8ALAAAAAAgACAAAAf+gH+Cg4SFhoeIiYIAAIqOi42DAGJikZCPkpSWAFxcm5qIjIQAT02b\nICWflaONADxGln8UIoUPG4UpK6NIOYyggxUDhaKEBi+jYmCtSrEVsX/EkseSUZsNhMEZhBvXgxkA\n04IDz80olikvJ+EAD+Ehz9CWFTi3gg87NfV/ICTr8OwVBM3jYWARkiCRDPDoJ6jBBAWGHtToNi9L\nQWhcnkRqwIXhnwozQBjq10PYPDEuRG6gBBGkGIYAjKAINyjkSxATcIiBdeEFJRHOnrxkMcGnhB2G\neCgQE8UAAJ1inO2gRANACEokBjzIsgXAkEMArojpZQNJkRPgYMBAy8LHkXfYP8QwC4WBwoJxjPLq\n1UvAgIMJBxD9bWGDR5EoUxJTSpZ4ypMhPGqsgDAB0YsJYhdr3rwZiQIciTJgGOIDx4wXL0ioVj3z\nRY0cPoY8oKWIALsMJFqj3p2axIUGABBgGpCFs3ExTuCF4qEjBorV0EmsmLEDh3KwACqEYIG6Bg4c\nNFCvwBmt9o0d4VFHX4EaBo4eNa4PigBgQAUPq3m/WLG6AnAAPigCQA/HFbiFCDQZgpYCGZzg3ncQ\nQnhDahc4hZQiQPAw4XMeVODhh/zMhAMPQmBi4okoPhIIADs=\n',
    'blackPawn': b'R0lGODlhIAAgAMYAAAAAAAICAgQEBAcHBwkJCQsLCw0NDRAQEBMTExUVFRgYGBsbGx4eHiEhISQk\nJCsrKy8vLzIyMjY2Njs7Oz8/P0NDQ01NTVNTU1hYWGRkZGtra3Jycnl5eYGBgYODg4eHh5CQkJWV\nlZubm6Kioqenp62trbKysre3t7y8vMHBwcXFxcnJyc3NzdHR0dXV1djY2Nvb29/f3+Hh4eLi4uXl\n5ejo6Orq6u3t7fDw8PLy8vT09Pf39/n5+fv7+/39/f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH+\nEUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKADQALAAAAAAgACAAAAfmgDSCg4SFhoeIiYqLjI2OhTU/\nPzWPjD4pDw8rPpWJLS4AoQAuLJ2HOxeiABk7poYvIqolL66FJjkEoQY6IbWEPx0CoQIjnL40Pxmq\noSLGri0ty6IwKbU9qdIAGjq1PxHZABY/tTIe4CAutSgxAdIBMcc+H9IhPMctPxqqHT8qvjc8NAxQ\nVYBDj1o1ahwAl6AGvEovbhgAF0pBjhWVfCygKKrBOEczTnBUtSJdox8MRop68HHRiRcqVdUgwShG\nrJihSrRgtAMDzlAbbDD6AeEngAktE/3AcaOp06dQb+RIeqyq1auEAgEAOw==\n',
    'blackRook': b'R0lGODlhIAAgAMZIAAAAAAYGBgsLCw0NDRAQEBERERMTExUVFRgYGBkZGRsbGxwcHCQkJCcnJykp\nKSoqKisrKy0tLTAwMDIyMjU1NTc3Nzg4ODk5OTs7Oz4+PkNDQ0hISExMTE1NTVBQUFNTU1dXV15e\nXmRkZGdnZ2tra2xsbG5ubnBwcHNzc4GBgY6OjpCQkJ+fn6ampqenp7Gxsbm5ub+/v8HBwcXFxcbG\nxsnJyc3NzdHR0dTU1NXV1djY2NnZ2dra2t3d3erq6uvr6+3t7fDw8PT09Pb29vf39/n5+fz8/P39\n/f//////////////////////////////////////////////////////////////////////////\n////////////////////////////////////////////////////////////////////////////\n/////////////////////////////////////////////////////////////////////////yH+\nEUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAH8ALAAAAAAgACAAAAf+gH+Cg4SFhoeIiYqLhDc5OTeE\nj4+SjzaLSEJAQEFIgkebm0eCSEGbQp6JSA0AAANIsDWtrTWwSAWtDamIq60EJ8AZswAcwCcGrRe7\nh0gSw8/QsxLLhkgkHdjZ2tvZI9SFSDg6O+Tl5uc7OjnfhUcmC9HRCyhFjH9GKxUW+/z9+xUshtj7\nw0NWvGc1Vgz8Y/DgrBoLGTocBnFhw4kVB150mNHexoMdGX2MF3LRyGglFZ2EljIRjYkPF/4o4aGm\nzZs3TcSwJ6OHrZ9Af/Z4wQjJgABIkypdGsAAO3AIYA5D8FQQEVg+QmndqtUHLCKHiLR48CAChbNo\n06o9SxaGj2oaIKQePAEErtx4dA3lEDKpr9+/fflGHEw4YiAAOw==\n',
    'blackKnight': b'R0lGODlhIAAgAMZxAAAAAAQEBAYGBgcHBwkJCQoKCgsLCxAQEBMTExQUFBwcHB8fHyAgICIiIiMj\nIyQkJCUlJSYmJikpKSwsLC0tLS8vLzAwMDIyMjQ0NDk5OTo6Ojw8PD09PT4+Pj8/P0BAQEFBQUND\nQ0ZGRktLS09PT1BQUFNTU1RUVFZWVlhYWFtbW1xcXF5eXl9fX2BgYGVlZWhoaGlpaWtra2xsbG9v\nb3BwcHNzc3R0dHV1dXZ2dnd3d3h4eHl5eXp6en19fYCAgIGBgYKCgoODg4aGhoeHh4qKiouLi4yM\njI2NjY6Ojo+Pj5CQkJGRkZOTk5SUlJaWlpeXl5mZmZ2dnZ+fn6CgoKWlpaampqenp6urq6ysrK2t\nra+vr7Ozs7W1tbi4uLq6uru7u7y8vL+/v8LCwsPDw8rKysvLy83Nzc7Ozs/Pz9PT09fX19jY2N/f\n3+vr6+/v7/f39////////////////////////////////////////////////////////////yH+\nEUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAH8ALAAAAAAgACAAAAf+gH+Cg4SFhoeIiYqLhzWFWoyM\nTRxHgzkURJGKPQQLTU45BgBBmokpHQAZLREAACxEYWg9pYRbIK24ABUMbWxaVku0aVcDua0OrQw/\nbE5kpV8Sxq0EuQdbR16RNyYAIU7SxgFYSlWMRMVWF+DhYjBTikQerQfr0g9gPiyIbzn1/kIyIB0y\nAsEfAAHgFJDBgQiHwQYJ1nFh8cTQjg3+LChpsM5FlCyGbPhLIKULR3AT1vAoJKNCvQhMShDx9yZG\nISataEjbsEWQw3pgdBSiAi7ACySCiITwB6UioTEIWj1YAKBAkhODitCr9wMkoR04AgAAgSBAJkFw\nmHAwOMOMISFOVJYEWTBkx6AyGgwCWOEmURosTgadwaAXwIc4mpqMKAxABGJGKlAwBjDi8SIdDyaX\nsKxI5GQUnBNJnrwiNKIXJFKrXs2aBBA1tGLLphUIADs=\n',
    'blackBishop': b'R0lGODlhIAAgAMYAAAAAAAICAgMDAwQEBAUFBQcHBwkJCQsLCwwMDA0NDQ4ODg8PDxAQEBERERMT\nExUVFRcXFxgYGBkZGRsbGxwcHB0dHR4eHiAgICEhISIiIiMjIyQkJCYmJicnJysrKywsLC0tLS4u\nLjAwMDExMTIyMjMzMzQ0NDY2Njc3Nzk5OTs7Oz4+Pj8/P0BAQEFBQUVFRUZGRkdHR0hISExMTE1N\nTVBQUFFRUVNTU1RUVFdXV1hYWFxcXF5eXmFhYWNjY2RkZGZmZmtra2xsbG5ubnBwcHV1dXd3d3t7\ne39/f4GBgYiIiIqKio6OjpCQkJqamp2dnZ+fn6CgoKOjo6WlpampqaqqqrCwsLGxsbKysrW1tba2\ntre3t7m5ubq6uru7u729vcHBwcPDw8jIyMnJycrKyszMzM3Nzc7Ozs/Pz9LS0tPT09TU1NXV1dbW\n1tnZ2dvb297e3uDg4OHh4eLi4uPj4+Xl5ebm5ujo6O3t7fDw8PX19fj4+AAAAAAAAAAAAAAAACH+\nEUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAH8ALAAAAAAgACAAAAf+gH+Cg4SFhoeIiX9vSmOKj4dz\nDwAFYZCXgkUAmxiYl1ALmyaekHA6DiNppIpwVBoBEUB5q4dmIQGbmxBWtIRZHLnBEDe9f2QbwQPB\nCEC0cCfBADTRFmirXA65Bg5BDgzBLKRTM8EPHk0eHcEYep5cKNHS8QV4nmIk8d/RAvWYWC3xAkKQ\nQ2oLgYDRRpxZtUIZQgAXxNASMuMEjYsYacjwAKXXixS4BGrp1UTAQwAfaAXZ4aGly5ceYpBZVQUG\nzJsgeJGKou6kAWur0sSAUCBagAYiuhSDEueNFxIKKCxRQ4cNJjBXnuzowWOICxUiJm0ywKHECx4+\neOBIYkVioTFBGEyePBmgAhhCZSDkQnCgr18JJGy8wKDAr9+DAAxUGdSGzA8nZ+DcmTzZzposSKiU\noUN5cp00WIwU2VOstOlBgQAAOw==\n',
    'blackKing': b'R0lGODlhIAAgAMZpAAAAAAMDAwQEBAYGBggICAsLCwwMDBAQEBQUFBgYGBkZGRsbGxwcHCAgICEh\nISQkJCYmJigoKCkpKSoqKiwsLC0tLS8vLzAwMDMzMzQ0NDY2Njc3Nzw8PD09PT4+Pj8/P0BAQEJC\nQkREREVFRUdHR0xMTE9PT1BQUFRUVFZWVlhYWFlZWVpaWltbW1xcXF5eXl9fX2BgYGFhYWJiYmNj\nY2RkZGZmZmdnZ2hoaGxsbG1tbW5ubm9vb3BwcHFxcXR0dHZ2dnd3d3h4eHl5eXp6enx8fH19fX9/\nf4CAgIGBgYODg4WFhYeHh4iIiImJiYuLi42NjY6Ojo+Pj5GRkZmZmZqampycnJ2dnZ+fn7CwsLS0\ntLe3t7q6uru7u7y8vL+/v8HBwdvb29/f3+Pj4+vr6+/v7/Pz8/f39/v7+///////////////////\n/////////////////////////////////////////////////////////////////////////yH+\nEUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAH8ALAAAAAAgACAAAAf+gH+Cg4SFhoeIiYNpio2IaWlM\nkI6Uf2lfWCZYX4yVjZBHk56OaaGjlGlPnaeJYx0NH2OsjxwAthtop5C7nWABtrZXgryihmldMiEj\nLlqQS8C2M2llQiceJTtlq4szKDE13yoaW1XQAEg0Di7gNTgrTdtpUEIJ0Ak5LDUVwAwUKjgHoF3w\nUWWVmR8MzNmiAEQCsAVKGigEkOAHmWFWeky0ZcDIAAAClBjYCKCGFEZpeAghCeBAEABE6pGs4QMl\nkZUsRbhQwRLADyedxgwh0FNKzwRJyiyy8aNnDJYCgBTZhqYFkpEbZU40kATGNkFoXkzJAOBBjSI4\nesTAEaMtOBGJAmxdaCLtURQhP0pg3cgAnA4aVL4WSnOhpzkM2j4VtsUgAwgVbWOA4NAgLgAEgo2x\nwNFOBIUGRG01eADCBecUmQeTMAxtQmpChBdGjgzuG4i4mEnJ6IGjFskHOHLceL3IiwsLhiGcwEJ8\nGKQzS0RYYFDA1gAFETr0GLPLEzExXLKEOcNrlnlBgQAAOw==\n',
    'blackQueen': b'R0lGODlhIAAgAOejAAAAAAICAgMDAwQEBAYGBgcHBwgICAkJCQoKCgwMDA0NDQ8PDxAQEBERERIS\nEhMTExQUFBUVFRYWFhgYGBkZGRsbGxwcHB0dHR8fHyAgICEhISIiIiMjIyQkJCUlJSYmJigoKCkp\nKSoqKiwsLDAwMDExMTMzMzQ0NDU1NTg4ODk5OTo6Ojs7Ozw8PD09PT4+Pj8/P0BAQEJCQkNDQ0RE\nREVFRUdHR0hISEpKSktLS0xMTE1NTU5OTk9PT1BQUFFRUVJSUlNTU1RUVFVVVVdXV1lZWVpaWltb\nW1xcXF5eXl9fX2BgYGFhYWJiYmRkZGVlZWZmZmhoaGlpaWpqamtra2xsbG5ubnBwcHFxcXJycnNz\nc3R0dHZ2dnd3d3h4eHl5eXp6ent7e319fX5+foCAgIGBgYODg4SEhIWFhYaGhoeHh4iIiImJiYqK\niouLi4yMjI2NjY+Pj5CQkJGRkZKSkpSUlJWVlZeXl5iYmJmZmZqampubm5ycnJ2dnZ+fn6CgoKKi\noqOjo6SkpKWlpaampqenp6qqqq2tra6urq+vr7CwsLKysrOzs7S0tLW1tba2tre3t7m5ubu7u729\nvb6+vr+/v8XFxcfHx8jIyNDQ0NTU1NnZ2dvb297e3t/f3+Hh4ebm5ufn5+/v7///////////////\n////////////////////////////////////////////////////////////////////////////\n////////////////////////////////////////////////////////////////////////////\n////////////////////////////////////////////////////////////////////////////\n////////////////////////////////////////////////////////////////////////////\n/////////////////////////////////////////////////////yH5BAEKAP8ALAAAAAAgACAA\nAAj+AP8JHEiwoMGDCBP+i3TEiSOFEBnB+DHQCxAAAJrkGTiHDhqIAsXAwFhFoJWLGR+ZJJnjYBw+\nVgQeMYKxy0BDPpT8GRgEYxAmAqlEqvPPkowQbjwJxBNlTcyBcPAQRGTCBCKBS8Js6JHIDEYSXga6\n0VKQCpiCZS4NFEQBI59CGHsQGbjmBUE3NYo0IYhip8A3KgAoiPSvUJo7BNcUsDOwkYYUam4SEEQw\nTxpDA/2U4DPwDQAkAwcBWABoIBQAigYianGGYBoeRLYIhAPgAuV/azC2EcgIA4BDvHNAuUKwixQF\na2ZjPPuPCsYsAr9gXPTvjZwBYjYSJAOARh/cGG/+0PmHA6ORf4hmYHyIaQUAOAYDAQgw5Uju2ngg\nicDoglAfCBg9AskRADhAWEGbJACABIu4gREAU1Ty4AKdEPFgJo4gAMAGlBikyQcY2SDIgx949mAe\nEjzIiQkYsXAbQZPIgNEAPTwIwH4PhmCjEA8S4YZBjPCIUQMRWLDBBhdwoCQHHoCwQQcZZAAgAE+Q\nZdAVFTAggI1cdgnAARRcMN5BjEzp5ZkPXpBIQnVoiOaZExCi0B9jxGDnnXjeSYOdNNhgBxcQXXLC\nm13SABxEgOzAZQJRRmkAl1RYqVAjQ9xwgw862DlClCTY6YMPN9CQhB4gpUCol08ldIkMduqAxBI/\nedopxBKX2olFZAlhcaqXDxSikCMlTLArRgVU0MInCm0iyiieIGJHHGZ0Ie20bMSxhyShjALKICB1\n6+233wYEADs=\n',
    'blank': b'R0lGODlhIAAgAIAAAP///////yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAEALAAAAAAgACAA\nAAIejI+py+0Po5y02ouz3rz7D4biSJbmiabqyrbuC5sFADs=\n'
    }

class App():
    def __init__(self, master):
        (self.x0, self.y0) = (None, None)

        frame = Frame(master, relief='raised', borderwidth=1)
        frame.grid(row=1, pady=5, padx=5)
        frame.columnconfigure(1, weight=1)

        title = Frame(master)
        title.grid(row=0, pady=5, padx=5, sticky='EW')
        title.columnconfigure([0,1], weight=1)

        self.turn_text = StringVar()
        self.turn = Label(title, textvariable=self.turn_text)
        self.turn.grid(row=0, column=0, sticky='W')

        self.message_text = StringVar()
        self.message = Label(title, textvariable=self.message_text)
        self.message.grid(row=0, column=1, sticky='E')

        self.undo = Button(title, command=board.undo, text='Undo')
        self.undo.grid(row=1, column=0, sticky='W')

        #Generate 8x8 grid of buttons, which pass their coordinates to click()
        self.button = {}
        for x in range(8):
            Label(frame, text=columns[x], relief='groove').grid(row=9, column=x+1)
            for y in range(8):
                Label(frame, width=2, text=y+1).grid(row=8-y)
                self.button[(x,y)] = Button(frame, command=lambda x=x,y=y: app.click(x,y))
                self.button[(x,y)].grid(column=x+1, row=8-y)

                #Color alternating squares
                if x%2 == y%2:
                    self.button[(x,y)]['background'] = 'gray'
                    self.button[(x,y)]['foreground'] = 'white'

        self.update()

    #Display piece icons in occupied squares
    def update(self):
        self.turn_text.set(colors[board.turn].title()+'\'s Turn')
        for x in range(8):
            for y in range(8):
                if board.squares[(x,y)] != None:
                    self.button[(x,y)].img = PhotoImage(data=icons[self.imgname(x,y)])
                    self.button[(x,y)]['image'] = self.button[(x,y)].img
                else:
                    self.button[(x,y)].img = PhotoImage(data=icons['blank'])
                    self.button[(x,y)]['image'] = self.button[(x,y)].img

    def imgname(self, x, y):
        return str(colors[board.squares[(x,y)].color] + board.squares[(x,y)].__class__.__name__)

    def click(self, x,y):
        #First click must be an occupied square containing the correct color piece
        if (self.x0, self.y0) == (None, None):
            if getattr(board.squares[(x,y)], 'color', None) is board.turn:
                (self.x0, self.y0) = (x, y)
                app.button[(self.x0, self.y0)]['relief'] = 'sunken'
            elif getattr(board.squares[(x,y)], 'color', None) is (board.turn+1)%2:
                self.message_text.set("That's not your piece!")
            else:
                self.message_text.set("There's no piece here!")

        #Second click passes chosen piece and destination to move(), then erases first click coords
        else:
            if board.valid_move(board.squares[(self.x0, self.y0)], x, y):
                board.squares[(self.x0, self.y0)].move(x, y)
                board.check()
            app.button[(self.x0, self.y0)]['relief'] = 'raised'
            (self.x0, self.y0) = (None, None)



class Board():
    def __init__(self):
        self.x0 = self.y0 = None
        self.turn = 0
        self.in_check = False
        self.squares = {}
        self.kings, self.moves = [], []
        self.pieces = [[],[]]

    #Clear all squares, then add pieces at starting positions
    def reset(self):
        for x in range(8):
            for y in range(8):
                self.squares[(x,y)] = None
        for x in range(8):
            Pawn(x,1,0)
            Pawn(x,6,1)
        for x in (0,7):
            Rook(x,0,0)
            Rook(x,7,1)
        for x in (1,6):
            Knight(x,0,0)
            Knight(x,7,1)
        for x in (2,5):
            Bishop(x,0,0)
            Bishop(x,7,1)
        Queen(3,0,0)
        Queen(3,7,1)
        self.kings.append(King(4,0,0))
        self.kings.append(King(4,7,1))

    def valid_move(self, piece, x ,y):
        return piece.can_move(x, y) and not piece.is_blocked(x, y)

    def move(self, piece, x, y):
        if self.can_move(x,y):
            #Just a regular old move
            if (board.squares[(x,y)] == None):
                self.erase()
                self.posx, self.posy = x, y
                self.moved = True
                board.squares[(x,y)] = self
                board.turn = (self.color+1)%2
                app.message_text.set('')
            #Kill the enemy and stand on his grave
            elif (board.squares[(x,y)].color != self.color):
                self.erase()
                self.posx, self.posy = x, y
                self.moved = True
                board.squares[(x,y)].kill()
                board.squares[(x,y)] = self
                board.turn = (self.color+1)%2
                app.message_text.set('')
            #No friendly fire!
            elif board.squares[(x,y)].color == self.color:
                print("Target square is already occupied!")
                app.message_text.set("Target square is already occupied!")
        else:
            print("Invalid move.")
            app.message_text.set("Invalid move.")
        print(board.moves)
        app.update()


    def undo(self):
        if len(board.moves) > 0:
            last_turn = self.moves.pop()
            self.turn = (self.turn+1)%2
            for piece in last_turn.keys():
                board.squares[last_turn[piece]] = piece
                if piece != None:
                    (piece.posx, piece.posy) = last_turn[piece]
            app.update()

    def check(self):
        for enemy in self.pieces[(self.turn)]:
            if self.valid_move(enemy, self.kings[(self.turn+1)%2].posx, self.kings[(self.turn+1)%2].posy):
                if self.in_check == False:
                    app.message_text.set("Don't put yourself in check!")
                else:
                    app.message_text.set("You must protect the King!")
                self.undo()
                return True
        for enemy in self.pieces[(self.turn+1)%2]:
            if self.valid_move(enemy, self.kings[self.turn].posx, self.kings[self.turn].posy):
                app.message_text.set("Check! Protect your King!")
                self.in_check = True
                return True
        return False


##moves = [ {Pawn1:(x,y), None:(x,y)}, {Pawn2:(x,y), None:(x,y)} ]


class Piece():
    def __init__(self, posx, posy, color):
        self.posx = posx
        self.posy = posy
        self.color = color
        self.moved = False
        board.squares[(posx,posy)] = self
        board.pieces[self.color].append(self)

    # This block doesn't work, and probably isn't worth doing anyway.
    # def __eq__(self, other):
    #     return self.color == getattr(other, 'color', None)
    #  def __hash__(self):
    #     return super(Piece, self).__hash__()

    def erase(self):
        board.squares[(self.posx,self.posy)] = None
        self.posx, self.posy = None, None

    def kill(self):
        self.erase()
        board.pieces[self.color].remove(self)

    def move(self, x, y):
        board.moves.append({self:(self.posx, self.posy), board.squares[(x,y)]:(x,y)})
        if self.is_attacking(x, y):
            board.squares[(x,y)].kill()
        self.erase()
        self.posx, self.posy = x, y
        self.moved = True
        board.squares[(x,y)] = self
        board.turn = (self.color+1)%2
        app.message_text.set('')
        app.update()

    def is_attacking(self, x, y):
        return getattr(board.squares[(x,y)], 'color', self.color) != self.color

    def is_blocked(self, x, y):
    #Friendly unit at target square, or any unit along travel path, blocks the move
        if getattr(board.squares[(x,y)], 'color', None) is self.color:
            return True
        #Normalize movement vectors xi,yi
        if (abs(x-self.posx) > 0):
            xi = int((x-self.posx)/abs(x-self.posx))
        else:
            xi = x-self.posx
        if (abs(y-self.posy) > 0):
            yi = int((y-self.posy)/abs(y-self.posy))
        else:
            yi = y-self.posy

        #Check each square between self and destination is empty, exclusive
        for n in range(1, max(abs(x-self.posx), abs(y-self.posy))):
            if board.squares[(self.posx + n*xi, self.posy + n*yi)] != None:
                return True
        return False

class Pawn(Piece):
    def can_move(self, x, y):
        if (y-self.posy == 1-2*self.color): #Determines if movement is 1-square "forward"
            if (x==self.posx) and (board.squares[(x,y)] == None):
                return True #Straight move
            elif abs(x-self.posx) == 1 and board.squares[(x,y)] != None:
                return True #Diagonal attack
        elif all([(self.moved==False), (self.posx==x), (y-self.posy==2-4*self.color),
                  (board.squares[(x,y)]==None)]):
            return not self.is_blocked(x,y)   #2-square opener
        return False

class Rook(Piece):
    def can_move(self, x, y):
       return ((x == self.posx) or (y == self.posy))

    def castle(self):
        self.move((self.posx+4)//2, self.posy)

class Bishop(Piece):
    def can_move(self, x, y):
        return (abs(x-self.posx) == abs(y-self.posy))

class Queen(Piece):
    def can_move(self, x, y):
        return Bishop.can_move(self, x, y) or Rook.can_move(self, x, y)

class Knight(Piece):
    def can_move(self, x, y):
        return ((abs(x-self.posx) == 1 and abs(y-self.posy) == 2) or
               (abs(x-self.posx) == 2 and abs(y-self.posy) == 1))
    def is_blocked(self, x, y): #Override: Can only be blocked at the target square
        return getattr(board.squares[(x,y)], 'color', None) is self.color

class King(Piece):
    def can_move(self, x, y):
        if ((abs(x - self.posx) <= 1) and (abs(y - self.posy) <= 1)):
            return True
        elif self.moved == False and y == self.posy and board.squares[(x,y)] == None:
            if x == 1 and board.squares[(0,y)].__class__ is Rook and board.squares[(0,y)].moved == False:
                board.squares[(0,y)].castle()
                return True
            elif x == 6 and board.squares[(7,y)].__class__ is Rook and board.squares[(7,y)].moved == False:
                board.squares[(7,y)].castle()
                return True
        return False
    def castle(self, x, y):
        pass





##def click(x,y):
##    #First click must be an occupied square containing the correct color piece
##    if board.x0 == None and board.y0 == None:
##        if board.squares[(x,y)] == None:
##            print("There's no piece here!")
##            app.message_text.set("There's no piece here!")
##
##        elif board.squares[(x,y)].color == board.turn:
##            (board.x0, board.y0) = (x, y)
####            app.button[(x,y)]['state'] = 'active'
##        else:
##            print("That's not your piece!")
##            app.message_text.set("That's not your piece!")
##    #Second click passes chosen piece and destination to move(), then erases first click coords
##    else:
##        board.squares[(board.x0,board.y0)].move(x, y)
##        board.x0 = board.y0 = None        





if __name__ == '__main__':

    root = Tk()
    board = Board()
    board.reset()
    app = App(root)
    root.mainloop()
