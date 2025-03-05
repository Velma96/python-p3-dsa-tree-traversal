class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        return self._dfs(self.root, target_id)

    def _dfs(self, node, target_id):
        if node['id'] == target_id:
            return node
        
        for child in node['children']:
            result = self._dfs(child, target_id)
            if result:
                return result

        return None
    def get_element_by_id(self, target_id):
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            node = nodes_to_visit.pop(0)

            if node['id'] == target_id:
                return node

            nodes_to_visit.extend(node['children'])

        return None

