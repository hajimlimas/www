import secrets

import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import MatchForm
from .models import HomeTeam, AwayTeam


def index(request):
    form = MatchForm()
    # form.fields['league'].queryset = League.objects.all()
    form.fields['home_team'].queryset = HomeTeam.objects.none()
    form.fields['away_team'].queryset = AwayTeam.objects.none()
    return render(request, 'index.html', {'form': form})


def about_view(request):
    return render(request, 'about.html')


def privacy_view(request):
    return render(request, 'privacy.html')


def terms_view(request):
    return render(request, 'terms.html')


def contact_view(request):
    return render(request, 'contact.html')


def result_view(request):
    return render(request, 'result.html')


def get_home_teams(request):
    league_id = request.GET.get('league_id')
    home_teams = HomeTeam.objects.filter(league_id=league_id)
    options = '<option value="">---------</option>'

    for team in home_teams:
        options += f'<option value="{team.pk}">{team.name}</option>'

    return JsonResponse(options, safe=False)


def get_away_teams(request):
    league_id = request.GET.get('league_id')
    away_teams = AwayTeam.objects.filter(league_id=league_id)
    options = '<option value="">---------</option>'

    for team in away_teams:
        options += f'<option value="{team.pk}">{team.name}</option>'

    return JsonResponse(options, safe=False)


def matrix():
    random_numbers = [secrets.randbelow(100) + 1 for _ in range(16)]
    random_matrix = np.array(random_numbers).astype(int).reshape(4, 4).T
    random_matrix = np.where(random_matrix % 2 == 0, 0, 1)
    child_matrix = np.transpose(random_matrix)

    h1 = "".join([str(random_matrix[i][0]) for i in range(len(random_matrix))])
    h2 = "".join([str(random_matrix[i][1]) for i in range(len(random_matrix))])
    h3 = "".join([str(random_matrix[i][2]) for i in range(len(random_matrix))])
    h4 = "".join([str(random_matrix[i][3]) for i in range(len(random_matrix))])
    h5 = "".join([str(child_matrix[i][0]) for i in range(len(child_matrix))])
    h6 = "".join([str(child_matrix[i][1]) for i in range(len(child_matrix))])
    h7 = "".join([str(child_matrix[i][2]) for i in range(len(child_matrix))])
    h8 = "".join([str(child_matrix[i][3]) for i in range(len(child_matrix))])

    r1c1 = random_matrix[0][0]  # Row 1, Column 1
    r1c2 = random_matrix[0][1]  # Row 1, Column 2

    if r1c1 == 1 and r1c2 == 0:
        h91 = 1
    elif r1c1 == 0 and r1c2 == 1:
        h91 = 1
    elif r1c1 == 1 and r1c2 == 1:
        h91 = 0
    else:
        h91 = 0

    r2c1 = random_matrix[1][0]  # Row 2, Column 1
    r2c2 = random_matrix[1][1]  # Row 2, Column 2

    if r2c1 == 1 and r2c2 == 0:
        h92 = 1
    elif r2c1 == 0 and r2c2 == 1:
        h92 = 1
    elif r2c1 == 1 and r2c2 == 1:
        h92 = 0
    else:
        h92 = 0

    r3c1 = random_matrix[2][0]  # Row 3, Column 1
    r3c2 = random_matrix[2][1]  # Row 3, Column 2

    if r3c1 == 1 and r3c2 == 0:
        h93 = 1
    elif r3c1 == 0 and r3c2 == 1:
        h93 = 1
    elif r3c1 == 1 and r3c2 == 1:
        h93 = 0
    else:
        h93 = 0

    r4c1 = random_matrix[3][0]  # Row 4, Column 1
    r4c2 = random_matrix[3][1]  # Row 4, Column 2

    if r4c1 == 1 and r4c2 == 0:
        h94 = 1
    elif r4c1 == 0 and r4c2 == 1:
        h94 = 1
    elif r4c1 == 1 and r4c2 == 1:
        h94 = 0
    else:
        h94 = 0

    hh9 = int(str(h91) + str(h92) + str(h93) + str(h94))
    h9_str = '{:04d}'.format(hh9)
    h9 = h9_str

    r1c3 = random_matrix[0][2]  # Row 1, Column 3
    r1c4 = random_matrix[0][3]  # Row 1, Column 4

    if r1c3 == 1 and r1c4 == 0:
        h101 = 1
    elif r1c3 == 0 and r1c4 == 1:
        h101 = 1
    elif r1c3 == 1 and r1c4 == 1:
        h101 = 0
    else:
        h101 = 0

    r2c3 = random_matrix[1][2]  # Row 2, Column 3
    r2c4 = random_matrix[1][3]  # Row 2, Column 4

    if r2c3 == 1 and r2c4 == 0:
        h102 = 1
    elif r2c3 == 0 and r2c4 == 1:
        h102 = 1
    elif r2c3 == 1 and r2c4 == 1:
        h102 = 0
    else:
        h102 = 0

    r3c3 = random_matrix[2][2]  # Row 3, Column 3
    r3c4 = random_matrix[2][3]  # Row 3, Column 4

    if r3c3 == 1 and r3c4 == 0:
        h103 = 1
    elif r3c3 == 0 and r3c4 == 1:
        h103 = 1
    elif r3c3 == 1 and r3c4 == 1:
        h103 = 0
    else:
        h103 = 0

    r4c3 = random_matrix[3][2]  # Row 4, Column 3
    r4c4 = random_matrix[3][3]  # Row 4, Column 4

    if r4c3 == 1 and r4c4 == 0:
        h104 = 1
    elif r4c3 == 0 and r4c4 == 1:
        h104 = 1
    elif r4c3 == 1 and r4c4 == 1:
        h104 = 0
    else:
        h104 = 0

    hh10 = int(str(h101) + str(h102) + str(h103) + str(h104))
    h10_str = '{:04d}'.format(hh10)
    h10 = h10_str

    rr1cc1 = child_matrix[0][0]  # Row 1, Column 1
    rr1cc2 = child_matrix[0][1]  # Row 1, Column 2

    if rr1cc1 == 1 and rr1cc2 == 0:
        h111 = 1
    elif rr1cc1 == 0 and rr1cc2 == 1:
        h111 = 1
    elif rr1cc1 == 1 and rr1cc2 == 1:
        h111 = 0
    else:
        h111 = 0

    rr2cc1 = child_matrix[1][0]  # Row 2, Column 1
    rr2cc2 = child_matrix[1][1]  # Row 2, Column 2

    if rr2cc1 == 1 and rr2cc2 == 0:
        h112 = 1
    elif rr2cc1 == 0 and rr2cc2 == 1:
        h112 = 1
    elif rr2cc1 == 1 and rr2cc2 == 1:
        h112 = 0
    else:
        h112 = 0

    rr3cc1 = child_matrix[2][0]  # Row 3, Column 1
    rr3cc2 = child_matrix[2][1]  # Row 3, Column 2

    if rr3cc1 == 1 and rr3cc2 == 0:
        h113 = 1
    elif rr3cc1 == 0 and rr3cc2 == 1:
        h113 = 1
    elif rr3cc1 == 1 and rr3cc2 == 1:
        h113 = 0
    else:
        h113 = 0

    rr4cc1 = child_matrix[3][0]  # Row 4, Column 1
    rr4cc2 = child_matrix[3][1]  # Row 4, Column 2

    if rr4cc1 == 1 and rr4cc2 == 0:
        h114 = 1
    elif rr4cc1 == 0 and rr4cc2 == 1:
        h114 = 1
    elif rr4cc1 == 1 and rr4cc2 == 1:
        h114 = 0
    else:
        h114 = 0

    hh11 = int(str(h111) + str(h112) + str(h113) + str(h114))
    h11_str = '{:04d}'.format(hh11)
    h11 = h11_str

    rr1cc3 = child_matrix[0][2]  # Row 1, Column 3
    rr1cc4 = child_matrix[0][3]  # Row 1, Column 4

    if rr1cc3 == 1 and rr1cc4 == 0:
        h121 = 1
    elif rr1cc3 == 0 and rr1cc4 == 1:
        h121 = 1
    elif rr1cc3 == 1 and rr1cc4 == 1:
        h121 = 0
    else:
        h121 = 0

    rr2cc3 = child_matrix[1][2]  # Row 2, Column 3
    rr2cc4 = child_matrix[1][3]  # Row 2, Column 4

    if rr2cc3 == 1 and rr2cc4 == 0:
        h122 = 1
    elif rr2cc3 == 0 and rr2cc4 == 1:
        h122 = 1
    elif rr2cc3 == 1 and rr2cc4 == 1:
        h122 = 0
    else:
        h122 = 0

    rr3cc3 = child_matrix[2][2]  # Row 3, Column 3
    rr3cc4 = child_matrix[2][3]  # Row 3, Column 4

    if rr3cc3 == 1 and rr3cc4 == 0:
        h123 = 1
    elif rr3cc3 == 0 and rr3cc4 == 1:
        h123 = 1
    elif rr3cc3 == 1 and rr3cc4 == 1:
        h123 = 0
    else:
        h123 = 0

    rr4cc3 = child_matrix[3][2]  # Row 4, Column 3
    rr4cc4 = child_matrix[3][3]  # Row 4, Column 4

    if rr4cc3 == 1 and rr4cc4 == 0:
        h124 = 1
    elif rr4cc3 == 0 and rr4cc4 == 1:
        h124 = 1
    elif rr4cc3 == 1 and rr4cc4 == 1:
        h124 = 0
    else:
        h124 = 0

    hh12 = int(str(h121) + str(h122) + str(h123) + str(h124))
    h12_str = '{:04d}'.format(hh12)
    h12 = h12_str

    if h91 == 1 and h101 == 0:
        h131 = 1
    elif h91 == 0 and h101 == 1:
        h131 = 1
    elif h91 == 1 and h101 == 1:
        h131 = 0
    else:
        h131 = 0

    if h92 == 1 and h102 == 0:
        h132 = 1
    elif h92 == 0 and h102 == 1:
        h132 = 1
    elif h92 == 1 and h102 == 1:
        h132 = 0
    else:
        h132 = 0

    if h93 == 1 and h103 == 0:
        h133 = 1
    elif h93 == 0 and h103 == 1:
        h133 = 1
    elif h93 == 1 and h103 == 1:
        h133 = 0
    else:
        h133 = 0

    if h94 == 1 and h104 == 0:
        h134 = 1
    elif h94 == 0 and h104 == 1:
        h134 = 1
    elif h94 == 1 and h104 == 1:
        h134 = 0
    else:
        h134 = 0

    hh13 = int(str(h131) + str(h132) + str(h133) + str(h134))
    h13_str = '{:04d}'.format(hh13)
    h13 = h13_str

    if h111 == 1 and h121 == 0:
        h141 = 1
    elif h111 == 0 and h121 == 1:
        h141 = 1
    elif h111 == 1 and h121 == 1:
        h141 = 0
    else:
        h141 = 0

    if h112 == 1 and h122 == 0:
        h142 = 1
    elif h112 == 0 and h122 == 1:
        h142 = 1
    elif h112 == 1 and h122 == 1:
        h142 = 0
    else:
        h142 = 0

    if h113 == 1 and h123 == 0:
        h143 = 1
    elif h113 == 0 and h123 == 1:
        h143 = 1
    elif h113 == 1 and h123 == 1:
        h143 = 0
    else:
        h143 = 0

    if h114 == 1 and h124 == 0:
        h144 = 1
    elif h114 == 0 and h124 == 1:
        h144 = 1
    elif h114 == 1 and h124 == 1:
        h144 = 0
    else:
        h144 = 0

    hh14 = int(str(h141) + str(h142) + str(h143) + str(h144))
    h14_str = '{:04d}'.format(hh14)
    h14 = h14_str

    if h131 == 1 and h141 == 0:
        h151 = 1
    elif h131 == 0 and h141 == 1:
        h151 = 1
    elif h131 == 1 and h141 == 1:
        h151 = 0
    else:
        h151 = 0

    if h132 == 1 and h142 == 0:
        h152 = 1
    elif h132 == 0 and h142 == 1:
        h152 = 1
    elif h132 == 1 and h142 == 1:
        h152 = 0
    else:
        h152 = 0

    if h133 == 1 and h143 == 0:
        h153 = 1
    elif h133 == 0 and h143 == 1:
        h153 = 1
    elif h133 == 1 and h143 == 1:
        h153 = 0
    else:
        h153 = 0

    if h134 == 1 and h144 == 0:
        h154 = 1
    elif h134 == 0 and h144 == 1:
        h154 = 1
    elif h134 == 1 and h144 == 1:
        h154 = 0
    else:
        h154 = 0

    hh15 = int(str(h151) + str(h152) + str(h153) + str(h154))
    h15_str = '{:04d}'.format(hh15)
    h15 = h15_str

    if h151 == 1 and r1c1 == 0:
        h161 = 1
    elif h151 == 0 and r1c1 == 1:
        h161 = 1
    elif h151 == 1 and r1c1 == 1:
        h161 = 0
    else:
        h161 = 0

    if h152 == 1 and r2c1 == 0:
        h162 = 1
    elif h152 == 0 and r2c1 == 1:
        h162 = 1
    elif h152 == 1 and r2c1 == 1:
        h162 = 0
    else:
        h162 = 0

    if h153 == 1 and r3c1 == 0:
        h163 = 1
    elif h153 == 0 and r3c1 == 1:
        h163 = 1
    elif h153 == 1 and r3c1 == 1:
        h163 = 0
    else:
        h163 = 0

    if h154 == 1 and r4c1 == 0:
        h164 = 1
    elif h154 == 0 and r4c1 == 1:
        h164 = 1
    elif h154 == 1 and r4c1 == 1:
        h164 = 0
    else:
        h164 = 0

    hh16 = int(str(h161) + str(h162) + str(h163) + str(h164))
    h16_str = '{:04d}'.format(hh16)
    h16 = h16_str

    # Check Validity
    if r1c3 == 1 and rr1cc2 == 0:
        jar1 = 1
    elif r1c3 == 0 and rr1cc2 == 1:
        jar1 = 1
    elif r1c3 == 1 and rr1cc2 == 1:
        jar1 = 0
    else:
        jar1 = 0

    if r2c3 == 1 and rr2cc2 == 0:
        jar2 = 1
    elif r2c3 == 0 and rr2cc2 == 1:
        jar2 = 1
    elif r2c3 == 1 and rr2cc2 == 1:
        jar2 = 0
    else:
        jar2 = 0

    if r3c3 == 1 and rr3cc2 == 0:
        jar3 = 1
    elif r3c3 == 0 and rr3cc2 == 1:
        jar3 = 1
    elif r3c3 == 1 and rr3cc2 == 1:
        jar3 = 0
    else:
        jar3 = 0

    if r4c3 == 1 and rr4cc2 == 0:
        jar4 = 1
    elif r4c3 == 0 and rr4cc2 == 1:
        jar4 = 1
    elif r4c3 == 1 and rr4cc2 == 1:
        jar4 = 0
    else:
        jar4 = 0

    if h111 == 1 and h161 == 0:
        hi1 = 1
    elif h111 == 0 and h161 == 1:
        hi1 = 1
    elif h111 == 1 and h161 == 1:
        hi1 = 0
    else:
        hi1 = 0

    if h112 == 1 and h162 == 0:
        hi2 = 1
    elif h112 == 0 and h162 == 1:
        hi2 = 1
    elif h112 == 1 and h162 == 1:
        hi2 = 0
    else:
        hi2 = 0

    if h113 == 1 and h163 == 0:
        hi3 = 1
    elif h113 == 0 and h163 == 1:
        hi3 = 1
    elif h113 == 1 and h163 == 1:
        hi3 = 0
    else:
        hi3 = 0

    if h114 == 1 and h164 == 0:
        hi4 = 1
    elif h114 == 0 and h164 == 1:
        hi4 = 1
    elif h114 == 1 and h164 == 1:
        hi4 = 0
    else:
        hi4 = 0

    # Valid
    if jar1 == 1 and hi1 == 0:
        valid1 = 1
    elif jar1 == 0 and hi1 == 1:
        valid1 = 1
    elif jar1 == 1 and hi1 == 1:
        valid1 = 0
    else:
        valid1 = 0

    if jar2 == 1 and hi2 == 0:
        valid2 = 1
    elif jar2 == 0 and hi2 == 1:
        valid2 = 1
    elif jar2 == 1 and hi2 == 1:
        valid2 = 0
    else:
        valid2 = 0

    if jar3 == 1 and hi3 == 0:
        valid3 = 1
    elif jar3 == 0 and hi3 == 1:
        valid3 = 1
    elif jar3 == 1 and hi3 == 1:
        valid3 = 0
    else:
        valid3 = 0

    if jar4 == 1 and hi4 == 0:
        valid4 = 1
    elif jar4 == 0 and hi4 == 1:
        valid4 = 1
    elif jar4 == 1 and hi4 == 1:
        valid4 = 0
    else:
        valid4 = 0

    valid = int(str(valid1) + str(valid2) + str(valid3) + str(valid4))
    valid_str = '{:04d}'.format(valid)

    # Check if valid_str matches any of H1, H2, H3 ... H16
    if valid_str in [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16]:
        return "valid"
    else:
        return "invalid"


def sincerity():
    # Check sincerity
    r1c1, r2c1, r3c1, r4c1, r1c2, r2c2, r3c2, r4c2, r1c3, r2c3, r3c3, r4c3, r1c4, r2c4, r3c4, r4c4, \
        rr1cc1, rr2cc1, rr3cc1, rr4cc1, rr1cc2, rr2cc2, rr3cc2, rr4cc2, rr1cc3, rr2cc3, rr3cc3, rr4cc3, \
        rr1cc4, rr2cc4, rr3cc4, rr4cc4, h91, h92, h93, h94, h101, h102, h103, h104, h111, h112, h113, h114, \
        h121, h122, h123, h124, h131, h132, h133, h134, h141, h142, h143, h144, h151, h152, h153, h154, h161, \
        h162, h163, h164 = matrix()

    # Compute the sum of H1
    h1_sum = 0
    if r1c1 == 0:
        h1_sum += 2
    else:
        h1_sum += 1

    if r2c1 == 0:
        h1_sum += 2
    else:
        h1_sum += 1

    if r3c1 == 0:
        h1_sum += 2
    else:
        h1_sum += 1

    if r4c1 == 0:
        h1_sum += 2
    else:
        h1_sum += 1

    # Compute the sum of H9
    h9_sum = 0
    if h91 == 0:
        h9_sum += 2
    else:
        h9_sum += 1

    if h92 == 0:
        h9_sum += 2
    else:
        h9_sum += 1

    if h93 == 0:
        h9_sum += 2
    else:
        h9_sum += 1

    if h94 == 0:
        h9_sum += 2
    else:
        h9_sum += 1

    # Compute the sum of H10
    h10_sum = 0
    if h101 == 0:
        h10_sum += 2
    else:
        h10_sum += 1

    if h102 == 0:
        h10_sum += 2
    else:
        h10_sum += 1

    if h103 == 0:
        h10_sum += 2
    else:
        h10_sum += 1

    if h104 == 0:
        h10_sum += 2
    else:
        h10_sum += 1

    # Compute the sum of H13
    h13_sum = 0
    if h131 == 0:
        h13_sum += 2
    else:
        h13_sum += 1

    if h132 == 0:
        h13_sum += 2
    else:
        h13_sum += 1

    if h133 == 0:
        h13_sum += 2
    else:
        h13_sum += 1

    if h134 == 0:
        h13_sum += 2
    else:
        h13_sum += 1

    sincere = (h1_sum + h9_sum + h10_sum + h13_sum) % 16

    if sincere == 1:
        sum_h1 = r1c1 + r2c1 + r3c1 + r4c1
        if sum_h1 in [0, 2, 4]:
            return sincere

    elif sincere == 2:
        sum_h2 = r1c2 + r2c2 + r3c2 + r4c2
        if sum_h2 in [0, 2, 4]:
            return sincere

    elif sincere == 3:
        sum_h3 = r1c3 + r2c3 + r3c3 + r4c3
        if sum_h3 in [0, 2, 4]:
            return sincere

    elif sincere == 4:
        sum_h4 = r1c4 + r2c4 + r3c4 + r4c4
        if sum_h4 in [0, 2, 4]:
            return sincere

    elif sincere == 5:
        sum_h5 = rr1cc1 + rr2cc1 + rr3cc1 + rr4cc1
        if sum_h5 in [0, 2, 4]:
            return sincere

    elif sincere == 6:
        sum_h6 = rr1cc2 + rr2cc2 + rr3cc2 + rr4cc2
        if sum_h6 in [0, 2, 4]:
            return sincere

    elif sincere == 7:
        sum_h7 = rr1cc3 + rr2cc3 + rr3cc3 + rr4cc3
        if sum_h7 in [0, 2, 4]:
            return sincere

    elif sincere == 8:
        sum_h8 = rr1cc4 + rr2cc4 + rr3cc4 + rr4cc4
        if sum_h8 in [0, 2, 4]:
            return sincere

    elif sincere == 9:
        sum_h9 = h91 + h92 + h93 + h94
        if sum_h9 in [0, 2, 4]:
            return sincere

    elif sincere == 10:
        sum_h10 = h101 + h102 + h103 + h104
        if sum_h10 in [0, 2, 4]:
            return sincere

    elif sincere == 11:
        sum_h11 = h111 + h112 + h113 + h114
        if sum_h11 in [0, 2, 4]:
            return sincere

    elif sincere == 12:
        sum_h12 = h121 + h122 + h123 + h124
        if sum_h12 in [0, 2, 4]:
            return sincere

    elif sincere == 13:
        sum_h13 = h131 + h132 + h133 + h134
        if sum_h13 in [0, 2, 4]:
            return sincere

    elif sincere == 14:
        sum_h14 = h141 + h142 + h143 + h144
        if sum_h14 in [0, 2, 4]:
            return sincere

    elif sincere == 15:
        sum_h15 = h151 + h152 + h153 + h154
        if sum_h15 in [0, 2, 4]:
            return sincere

    elif sincere == 0:
        sum_h16 = h161 + h162 + h163 + h164
        if sum_h16 in [0, 2, 4]:
            return sincere

    return "Oops! We detected an error in your input. Either the match is not scheduled or the date is wrong. " \
           "Kindly double check and try again"


def determine_winner(home_team, away_team):
    h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16 = matrix()
    # Formula 1
    # Binary numbers were converted to base 10 for ease of comparison
    # Convert H1 to H16 to base 10
    base10_h1 = int(h1, 2)
    base10_h2 = int(h2, 2)
    base10_h3 = int(h3, 2)
    base10_h4 = int(h4, 2)
    base10_h5 = int(h5, 2)
    base10_h6 = int(h6, 2)
    base10_h7 = int(h7, 2)
    base10_h8 = int(h8, 2)
    base10_h9 = int(str(h9), 2)
    base10_h10 = int(str(h10), 2)
    base10_h11 = int(str(h11), 2)
    base10_h12 = int(str(h12), 2)
    base10_h13 = int(str(h13), 2)
    base10_h14 = int(str(h14), 2)
    base10_h15 = int(str(h15), 2)
    base10_h16 = int(str(h16), 2)

    # For home team
    values_to_check = [1, 7, 5, 2, 10, 6, 15, 13]
    hm_total = 0

    # Checking h1
    if base10_h1 in values_to_check:
        hm_total += 1

    # Checking h3
    if base10_h3 in values_to_check:
        hm_total += 1

    # Checking h5
    if base10_h5 in values_to_check:
        hm_total += 1

    # Checking h7
    if base10_h7 in values_to_check:
        hm_total += 1

    # Checking h9
    if base10_h9 in values_to_check:
        hm_total += 1

    # Checking h11
    if base10_h11 in values_to_check:
        hm_total += 1

    # Checking h13
    if base10_h13 in values_to_check:
        hm_total += 1

    # Checking h15
    if base10_h15 in values_to_check:
        hm_total += 1

    # For away team.
    values_to_check = [1, 7, 5, 2, 10, 6, 15, 13]
    aw_total = 0

    # Checking h2
    if base10_h2 in values_to_check:
        aw_total += 1

    # Checking h4
    if base10_h4 in values_to_check:
        aw_total += 1

    # Checking h6
    if base10_h6 in values_to_check:
        aw_total += 1

    # Checking h8
    if base10_h8 in values_to_check:
        aw_total += 1

    # Checking h10
    if base10_h10 in values_to_check:
        aw_total += 1

    # Checking h12
    if base10_h12 in values_to_check:
        aw_total += 1

    # Checking h14
    if base10_h14 in values_to_check:
        aw_total += 1

    # Checking h16
    if base10_h16 in values_to_check:
        aw_total += 1

    # result_method1 = None
    if hm_total > aw_total:
        result_method1 = "Home Team will Win"
    elif aw_total > hm_total:
        result_method1 = "Away Team will Win"
    else:
        result_method1 = "It will be a draw"

    # Formula 2
    # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
    # Binary numbers were converted to base 10 for ease of comparison

    # Define the classes
    classes = [
        [5, 4],  # Class 1
        [12],  # Class 2
        [8, 2],  # Class 3
        [6, 3],  # Class 4
        [0, 13],  # Class 5
        [15],  # Class 6
        [11, 14],  # Class 7
        [10, 9],  # Class 8
        [7],  # Class 9
        [1],  # Class 10
    ]
    # Define figures to compare
    base10_h1 = int(h1, 2)
    base10_h7 = int(h7, 2)

    # Find the classes that contain h1 and h7
    h1_class = None
    h7_class = None
    for i, c in enumerate(classes):
        if base10_h1 in c:
            h1_class = i + 1
        if base10_h7 in c:
            h7_class = i + 1

    # Compare the classes and determine the winner
    # result_method2 = None
    if h1_class < h7_class:
        result_method2 = "Home Team will Win"
    elif h7_class < h1_class:
        result_method2 = "Away Team will Win"
    else:
        result_method2 = "It will be a draw"

    # Formula 3
    # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
    # Binary numbers were converted to base 10 for ease of comparison

    # Define the classes
    classes = [
        [13, 7],  # Class 1
        [14, 0],  # Class 2
        [11],  # Class 3
        [12, 8],  # Class 4
        [2],  # Class 5
        [9, 15],  # Class 6
        [1, 6],  # Class 7
        [3],  # Class 8
        [4],  # Class 9
        [10, 5],  # Class 10
    ]
    # Define figures to compare
    base10_h1 = int(h1, 2)
    base10_h7 = int(h7, 2)

    # Find the classes that contain h1 and h7
    h1_class = None
    h7_class = None
    for i, c in enumerate(classes):
        if base10_h1 in c:
            h1_class = i + 1
        if base10_h7 in c:
            h7_class = i + 1

    # Compare the classes and determine the winner
    # result_method3 = None
    if h1_class < h7_class:
        result_method3 = "Home Team will Win"
    elif h7_class < h1_class:
        result_method3 = "Away Team will Win"
    else:
        result_method3 = "It will be a draw"

    # Formula 4
    # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
    # Binary numbers were converted to base 10 for ease of comparison

    # Define the classes
    classes = [
        [3, 5, 9],  # Class 1
        [6, 14, 7],  # Class 2
        [11],  # Class 3
        [0, 2, 15],  # Class 4
        [10, 12, 8, 4],  # Class 5
        [1, 13],  # Class 6
    ]
    # Define figures to compare
    base10_h1 = int(h1, 2)
    base10_h7 = int(h7, 2)

    # Find the classes that contain h1 and h7
    h1_class = None
    h7_class = None
    for i, c in enumerate(classes):
        if base10_h1 in c:
            h1_class = i + 1
        if base10_h7 in c:
            h7_class = i + 1

    # Compare the classes and determine the winner
    # result_method4 = None
    if h1_class < h7_class:
        result_method4 = "Home Team will Win"
    elif h7_class < h1_class:
        result_method4 = "Away Team will Win"
    else:
        result_method4 = "It will be a draw"

    # Formula 5
    # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
    # Binary numbers were converted to base 10 for ease of comparison

    # Define the classes
    classes = [
        [13, 1, 5],  # Class 1
        [0],  # Class 2
        [6, 2],  # Class 3
        [11],  # Class 4
        [8],  # Class 5
        [12],  # Class 6
        [15, 9],  # Class 7
        [14, 10],  # Class 8
        [4, 3],  # Class 9
        [7],  # Class 10
    ]
    # Define figures to compare
    base10_h1 = int(h1, 2)
    base10_h7 = int(h7, 2)

    # Find the classes that contain h1 and h7
    h1_class = None
    h7_class = None
    for i, c in enumerate(classes):
        if base10_h1 in c:
            h1_class = i + 1
        if base10_h7 in c:
            h7_class = i + 1

    # Compare the classes and determine the winner
    # result_method5 = None
    if h1_class < h7_class:
        result_method5 = "Home Team will Win"
    elif h7_class < h1_class:
        result_method5 = "Away Team will Win"
    else:
        result_method5 = "It will be a draw"

    # Determine the final result based on the results of the five methods
    results = [result_method1, result_method2, result_method3, result_method4, result_method5]

    home_wins = results.count("Home Team will Win")
    away_wins = results.count("Away Team will Win")
    draws = results.count("It will be a draw")

    if home_wins >= 3:
        final_result = f"{home_team} will win"
    elif away_wins >= 3:
        final_result = f"{away_team} will win"
    elif draws >= 3:
        final_result = "It will be a draw"
    else:
        final_result = "Sorry, we cannot determine the winner of this match"

    return final_result


@csrf_exempt
def process_form(request):
    if request.method == 'POST':
        home_team = request.POST.get('home_team')
        away_team = request.POST.get('away_team')

        while True:
            # Check validity
            valid = matrix()
            if valid == "valid":
                # Check sincerity
                sincere = sincerity()
                if sincere == sincere:
                    # Determine the winner
                    final_result = determine_winner(home_team, away_team)
                    return JsonResponse({'result': final_result})
                else:
                    return JsonResponse({'result': 'Oops'})
            else:
                break
                # Generate new random numbers and continue the loop
        return JsonResponse({'result': 'An error occurred. Please try again.../'})
      
