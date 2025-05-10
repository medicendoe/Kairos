from sets.Block import Block

class BlockList:
    def __init__(self, *args):
        self._blocks: list[Block] = []
        self._ids = set()
        for item in args:
            self.append(item)

    def _validate_block(self, block):
        if not isinstance(block, Block):
            raise TypeError("Solo se pueden añadir objetos de la clase Block a BlockList")
        if block.id in self._ids:
            raise ValueError(f"El ID {block.id} ya existe en la BlockList")

    def append(self, block):
        self._validate_block(block)
        self._blocks.append(block)
        self._blocks.sort()
        self._ids.add(block.id)

    def __getitem__(self, index):
        return self._blocks[index]

    def __setitem__(self, index, block):
        old_block = self._blocks[index]
        if block.id != old_block.id:
            self._validate_block(block)
            self._ids.add(block.id)
            self._ids.remove(old_block.id)
        else:
            if not isinstance(block, Block):
                raise TypeError("Solo se pueden asignar objetos de la clase Block")
        self._blocks[index] = block
        self._blocks.sort()

    def __delitem__(self, index):
        block_to_remove = self._blocks[index]
        del self._blocks[index]
        self._ids.remove(block_to_remove.id)

    def __len__(self):
        return len(self._blocks)

    def __iter__(self):
        return iter(self._blocks)

    def __contains__(self, block):
        return block in self._blocks

    def __str__(self):
        return f"BlockList([{', '.join(str(block) for block in self._blocks)}])"

    def clear(self):
        self._blocks.clear()
        self._ids.clear()

    def index(self, block, start=0, end=None):
        if not isinstance(block, Block):
            raise TypeError("Se debe buscar un objeto de la clase Block")
        return self._blocks.index(block, start, end)

    def pop(self, index=-1):
        block_to_remove = self._blocks.pop(index)
        self._ids.remove(block_to_remove.id)
        return block_to_remove

    def sort(self, *, key=None, reverse=False):
        super(BlockList, self).__setattr__('_blocks', sorted(self._blocks, key=key, reverse=reverse))
    
    def get_params(self):
        return self._blocks, sorted(self._ids)