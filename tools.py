"""
AI Modal - AI弹窗组件工具
支持弹窗设计、动画、交互
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIModalTools:
    """
    AI弹窗组件工具
    支持：设计、动画、交互
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_modal(self, purpose: str, style: str = "modern") -> Dict:
        """设计弹窗"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请设计{style}风格的{purpose}弹窗：

请返回JSON格式：
{{
    "layout": "布局",
    "components": ["组件"],
    "animations": ["动画"],
    "interactions": ["交互"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"modal": content}

    def generate_modal_code(self, modal_type: str, framework: str = "react") -> str:
        """生成弹窗代码"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{framework} {modal_type}弹窗组件：

要求：
1. TypeScript
2. 动画效果
3. 键盘导航
4. 可访问性"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_drawer(self, position: str, framework: str = "react") -> str:
        """生成抽屉组件"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{framework} {position}抽屉组件：

要求：
1. 滑入动画
2. 遮罩层
3. 关闭按钮
4. 响应式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def generate_notification(self, types: List[str], framework: str = "react") -> str:
        """生成通知组件"""
        if not self.client:
            return "LLM客户端未配置"

        types_text = ", ".join(types)

        prompt = f"""请生成{framework}通知组件：

类型：{types_text}

要求：
1. 多种类型
2. 自动消失
3. 堆叠显示
4. 动画效果"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_toast(self, positions: List[str], framework: str = "react") -> str:
        """生成Toast组件"""
        if not self.client:
            return "LLM客户端未配置"

        positions_text = ", ".join(positions)

        prompt = f"""请生成{framework} Toast组件：

位置：{positions_text}

要求：
1. 多位置支持
2. 自动消失
3. 进度条
4. 可关闭"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def generate_tooltip(self, triggers: List[str], framework: str = "react") -> str:
        """生成Tooltip组件"""
        if not self.client:
            return "LLM客户端未配置"

        triggers_text = ", ".join(triggers)

        prompt = f"""请生成{framework} Tooltip组件：

触发方式：{triggers_text}

要求：
1. 智能定位
2. 多方向
3. 动画效果
4. 延迟显示"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500
        )

        return response.choices[0].message.content

    def design_dialog_system(self, use_case: str) -> Dict:
        """设计对话框系统"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{use_case}设计对话框系统：

请返回JSON格式：
{{
    "types": ["对话框类型"],
    "patterns": ["使用模式"],
    "accessibility": "可访问性",
    "animation": "动画方案"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"dialog": content}


def create_tools(**kwargs) -> AIModalTools:
    """创建弹窗工具"""
    return AIModalTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Modal Tools")
    print()

    # 测试
    modal = tools.design_modal("确认删除", "modern")
    print(json.dumps(modal, ensure_ascii=False, indent=2))
