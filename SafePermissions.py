def ADMember(type):
    A9IDPayload = ("{\n  \"member\":\n  {\n    \"MemberName\"        :\"%s\",\n    \"SearchIn\"          :\"DELTA.RL.DELTA.COM\",\n    \"MembershipExpirationDate\"  :\"\",\n    \"Permissions\":\n    [\n      {" \
            "\"Key\":\"UseAccounts\", \"Value\":true},\n      {" \
            "\"Key\":\"RetrieveAccounts\", \"Value\":true},\n      {" \
            "\"Key\":\"ListAccounts\", \"Value\":true},\n      {" \
            "\"Key\":\"AddAccounts\", \"Value\":false},\n      {" \
            "\"Key\":\"UpdateAccountContent\",\"Value\":false},\n      {" \
            "\"Key\":\"UpdateAccountProperties\",\"Value\":false},\n      {" \
            "\"Key\":\"InitiateCPMAccountManagementOperations\",\"Value\":false},\n      {" \
            "\"Key\":\"SpecifyNextAccountContent\",\"Value\":false},\n      {" \
            "\"Key\":\"RenameAccounts\", \"Value\":false},\n      {" \
            "\"Key\":\"DeleteAccounts\", \"Value\":false},\n      {" \
            "\"Key\":\"UnlockAccounts\", \"Value\":false},\n      {" \
            "\"Key\":\"ManageSafe\", \"Value\":false},\n      {" \
            "\"Key\":\"ManageSafeMembers\", \"Value\":false},\n      {" \
            "\"Key\":\"BackupSafe\", \"Value\":false},\n      {" \
            "\"Key\":\"ViewAuditLog\", \"Value\":true},\n      {" \
            "\"Key\":\"ViewSafeMembers\", \"Value\":true},\n      {" \
            "\"Key\":\"RequestsAuthorizationLevel\",\"Value\":0},\n      {" \
            "\"Key\":\"AccessWithoutConfirmation\",\"Value\":false},\n      {" \
            "\"Key\":\"CreateFolders\", \"Value\":false},\n      {" \
            "\"Key\":\"DeleteFolders\", \"Value\":false},\n      {" \
            "\"Key\":\"MoveAccountsAndFolders\",\"Value\":false}\n    ]" \
            "\n  }\n}" %type)
    return A9IDPayload

def SafeMember(type):
    AdminstratorPayload = "{\n  \"member\":\n  {\n    \"MemberName\"        :\"Administrator\",\n    \"SearchIn\"          :\"Vault\",\n    \"MembershipExpirationDate\"  :\"\",\n    \"Permissions\":\n    [\n      {" \
                          "\"Key\":\"UseAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"RetrieveAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"ListAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"AddAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"UpdateAccountContent\",\"Value\":true},\n      {" \
                          "\"Key\":\"UpdateAccountProperties\",\"Value\":true},\n      {" \
                          "\"Key\":\"InitiateCPMAccountManagementOperations\",\"Value\":true},\n      {" \
                          "\"Key\":\"SpecifyNextAccountContent\",\"Value\":true},\n      {" \
                          "\"Key\":\"RenameAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"DeleteAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"UnlockAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"ManageSafe\", \"Value\":true},\n      {" \
                          "\"Key\":\"ManageSafeMembers\", \"Value\":true},\n      {" \
                          "\"Key\":\"BackupSafe\", \"Value\":true},\n      {" \
                          "\"Key\":\"ViewAuditLog\", \"Value\":true},\n      {" \
                          "\"Key\":\"ViewSafeMembers\", \"Value\":true},\n      {" \
                          "\"Key\":\"RequestsAuthorizationLevel\",\"Value\":1},\n      {" \
                          "\"Key\":\"AccessWithoutConfirmation\",\"Value\":true},\n      {" \
                          "\"Key\":\"CreateFolders\", \"Value\":true},\n      {" \
                          "\"Key\":\"DeleteFolders\", \"Value\":true},\n      {" \
                          "\"Key\":\"MoveAccountsAndFolders\",\"Value\":true}\n    ]" \
                          "\n  }\n}"

    VaultAdminPayload = "{\n  \"member\":\n  {\n    \"MemberName\"        :\"Vault Admins\",\n    \"SearchIn\"          :\"Vault\",\n    \"MembershipExpirationDate\"  :\"\",\n    \"Permissions\":\n    [\n      {" \
                          "\"Key\":\"UseAccounts\", \"Value\":false},\n      {" \
                          "\"Key\":\"RetrieveAccounts\", \"Value\":false},\n      {" \
                          "\"Key\":\"ListAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"AddAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"UpdateAccountContent\",\"Value\":true},\n      {" \
                          "\"Key\":\"UpdateAccountProperties\",\"Value\":true},\n      {" \
                          "\"Key\":\"InitiateCPMAccountManagementOperations\",\"Value\":true},\n      {" \
                          "\"Key\":\"SpecifyNextAccountContent\",\"Value\":true},\n      {" \
                          "\"Key\":\"RenameAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"DeleteAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"UnlockAccounts\", \"Value\":true},\n      {" \
                          "\"Key\":\"ManageSafe\", \"Value\":true},\n      {" \
                          "\"Key\":\"ManageSafeMembers\", \"Value\":true},\n      {" \
                          "\"Key\":\"BackupSafe\", \"Value\":true},\n      {" \
                          "\"Key\":\"ViewAuditLog\", \"Value\":true},\n      {" \
                          "\"Key\":\"ViewSafeMembers\", \"Value\":true},\n      {" \
                          "\"Key\":\"RequestsAuthorizationLevel\",\"Value\":1},\n      {" \
                          "\"Key\":\"AccessWithoutConfirmation\",\"Value\":true},\n      {" \
                          "\"Key\":\"CreateFolders\", \"Value\":true},\n      {" \
                          "\"Key\":\"DeleteFolders\", \"Value\":true},\n      {" \
                          "\"Key\":\"MoveAccountsAndFolders\",\"Value\":true}\n    ]" \
                          "\n  }\n}"

    if type == "Vault Admins":
        return VaultAdminPayload
    elif type == "Administrator":
        return AdminstratorPayload
