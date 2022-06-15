class Processor:
    # 全局处理器
    def __init__(self, process: callable = None):
        if process:
            self.process = process
        pass

    def process(self, w):
        raise NotImplementedError
