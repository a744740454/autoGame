CREATE TABLE gameAccounts (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- 主键，自动递增
    userId VARCHAR(255) NOT NULL,              -- 用户 ID
    password VARCHAR(255) NOT NULL,            -- 密码
    status VARCHAR(255) NOT NULL,              -- 状态 1.在售 2.训练中 3.是否售出
    datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 创建时间
    workType VARCHAR(255),
    gameType VARCHAR(255) NOT NULL,            -- 游戏类型 0 fate
    data TEXT                                  -- 数据
);