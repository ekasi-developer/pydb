class TableInterface:
    def __init__(self):
        """Load connection"""
        pass

    def create_table(self, table: str, columns: dict) -> bool:
        """Create table in database"""
        pass
    
    def update_table(self, table: str, columns: dict) -> bool:
        """Create table in database"""
        pass

    def delete_table(self, table: str) -> bool:
        """Delete table in database"""
        pass

    def table_exists(self, table: str) -> bool:
        """Check if table exist in database"""
        pass
