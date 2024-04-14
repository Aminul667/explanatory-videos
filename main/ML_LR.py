from manim import *


class TableExamples(Scene):
    def construct(self):
        data = [
            [1200, 25000],
            [1500, 30000],
            [1800, 35000]
        ]
        table = IntegerTable(
            data,
            # row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("Size"), Text("Price")],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": YELLOW}
        )

        col_labs = table.get_col_labels()
        
        col_labs.set_color(RED)
        table.scale(0.5)

        self.play(FadeIn(table), run_time=3)
        self.wait()
