def convert_date_format(date_str : str) -> str:
      day, month, year = date_str.split('-')
      return f"{year}-{month}-{day}"

def xp_req_logic(level : int, xp_req : int) -> int:
    return xp_req + (50*level)

    
def level_up_logic(xp : int, xp_req : int, level : int) -> tuple[int, int]:
    while xp >= xp_req:
        level = level + 1
        xp = xp - xp_req
        xp_req = xp_req_logic(level, xp_req)
    return xp, level 
    
